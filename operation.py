from PIL import Image, ImageTk
import numpy as np
import torch
import cv2
from model import UNet
from torchvision import transforms

def give_filepath_and_turn_gray(filepath):
    img = Image.open(filepath).convert('L').resize((512,512))    #读取输入图片并转换为灰度图
    output_path = './tmp_for_app/real_gray_image.png'
    img.save(output_path)    #将灰度图保存到临时路径下
    return output_path

def give_filepath_and_get_4_patch(filepath):
    img = Image.open(filepath)
    image_size = 512    #每张图像调整为512×512分辨率
    patch_size = 256    #每个块的大小是256×256分辨率

    #获取第1个切片
    x = 0
    y = 0
    patch_img_1 = img.crop(( x , y , x + patch_size , y + patch_size ))    #根据x和y坐标裁剪图像
    output_path_1 = './tmp_for_app/real_patch_image_1.png'
    patch_img_1.save(output_path_1)

    #获取第2个切片
    x = patch_size
    y = 0
    patch_img_2 = img.crop(( x , y , x + patch_size , y + patch_size ))    #根据x和y坐标裁剪图像
    output_path_2 = './tmp_for_app/real_patch_image_2.png'
    patch_img_2.save(output_path_2)

    #获取第3个切片
    x = 0
    y = patch_size
    patch_img_3 = img.crop(( x , y , x + patch_size , y + patch_size ))    #根据x和y坐标裁剪图像
    output_path_3 = './tmp_for_app/real_patch_image_3.png'
    patch_img_3.save(output_path_3)

    #获取第4个切片
    x = patch_size
    y = patch_size
    patch_img_4 = img.crop(( x , y , x + patch_size , y + patch_size ))    #根据x和y坐标裁剪图像
    output_path_4 = './tmp_for_app/real_patch_image_4.png'
    patch_img_4.save(output_path_4)

    return output_path_1, output_path_2, output_path_3, output_path_4

def give_filepath_and_equalize_patch(filepath):
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    equ = cv2.equalizeHist(img)    #直方图均衡化操作
    number = filepath[-5]
    output_path = './tmp_for_app/real_equalized_patch_image_' + number + '.png'
    cv2.imwrite(output_path, equ)    #保存直方图均衡化后的图像
    return output_path

def give_filepath_and_predict_mask(filepath):

    transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.5,),(0.5))
        ])

    # 加载模型
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    net = UNet(in_channels=1, num_classes=1)
    net.load_state_dict(torch.load('UNet_equalized_patch_256_50.pth', map_location=device))
    net.to(device)

    # 测试模式
    net.eval()
    with torch.no_grad():

        img = Image.open(filepath)    #读取预测的图片
        img = transform(img)    #预处理
        img = torch.unsqueeze(img,dim = 0)    #增加batch维度

        pred = net(img.to(device))    #网络预测

        pred = torch.squeeze(pred)    #将(batch、channel)维度去掉
        pred = np.array(pred.data.cpu())    #保存图片需要转为cpu处理

        pred[pred >=0 ] =255    #转为二值图片
        pred[pred < 0 ] =0

        pred = np.uint8(pred)    #转为图片的形式
        
        number = filepath[-5]
        output_path = './tmp_for_app/real_patch_mask_' + number + '.png'
        cv2.imwrite(output_path, pred)    #保存图片
        
    return output_path

def give_filepath_and_concatenate_mask(filepath_1, filepath_2, filepath_3, filepath_4):
    image_size = 512
    patch_size = 256
    
    img_1 = Image.open(filepath_1)
    img_2 = Image.open(filepath_2)
    img_3 = Image.open(filepath_3)
    img_4 = Image.open(filepath_4)

    mask = np.zeros(( image_size , image_size ))    #初始化输出掩码

    mask[ 0 : patch_size , 0 : patch_size ] = img_1
    mask[ 0 : patch_size , patch_size : 2 * patch_size ] = img_2
    mask[ patch_size : 2 * patch_size , 0 : patch_size ] = img_3
    mask[ patch_size : 2 * patch_size , patch_size : 2 * patch_size ] = img_4

    mask = np.uint8( mask )    #转为图片的形式
    
    output_path = './tmp_for_app/real_mask_without_attention.png'
    cv2.imwrite(output_path, mask )    #保存图片
    
    return output_path

def give_filepath_and_add_attention(filepath):
    image_size = 512
    dist = 235    #与中心像素点距离超过dist被认为是不感兴趣区域
    center_x = image_size // 2
    center_y = image_size // 2
    
    img = Image.open(filepath)    #读取图片
    img_array = np.array(img)    #将图片转换为数组
    
    for x_m in range( image_size ):
        for y_m in range( image_size ):
            d = (( x_m - center_x )**2 + ( y_m - center_y )**2)**( 1/2 )
            if d > dist:
                img_array[ x_m , y_m ] = 0

    img = np.uint8(img_array)    #将数组转换为图片
                
    output_path = './tmp_for_app/real_mask_with_attention.png'
    cv2.imwrite(output_path, img )    #保存图片
    
    return output_path

def give_image_filepath_and_seg(filepath):
    gray_filepath = give_filepath_and_turn_gray(filepath)
    patch_filepath_1, patch_filepath_2, patch_filepath_3, patch_filepath_4 = give_filepath_and_get_4_patch(gray_filepath)
    equalized_patch_1_filepath = give_filepath_and_equalize_patch(patch_filepath_1)
    equalized_patch_2_filepath = give_filepath_and_equalize_patch(patch_filepath_2)
    equalized_patch_3_filepath = give_filepath_and_equalize_patch(patch_filepath_3)
    equalized_patch_4_filepath = give_filepath_and_equalize_patch(patch_filepath_4)
    predicted_mask_1_filepath = give_filepath_and_predict_mask(equalized_patch_1_filepath)
    predicted_mask_2_filepath = give_filepath_and_predict_mask(equalized_patch_2_filepath)
    predicted_mask_3_filepath = give_filepath_and_predict_mask(equalized_patch_3_filepath)
    predicted_mask_4_filepath = give_filepath_and_predict_mask(equalized_patch_4_filepath)
    concatenated_mask_filepath = give_filepath_and_concatenate_mask(predicted_mask_1_filepath, predicted_mask_2_filepath, predicted_mask_3_filepath, predicted_mask_4_filepath)
    attention_mask_filepath = give_filepath_and_add_attention(concatenated_mask_filepath)
    return attention_mask_filepath
            
def give_filepath_and_split(filepath):

    transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.5,),(0.5))
        ])

    # 加载模型
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    net = UNet(in_channels=1, num_classes=1)
    net.load_state_dict(torch.load('UNet.pth', map_location=device))
    net.to(device)

    # 测试模式
    net.eval()
    with torch.no_grad():

        img = Image.open(filepath)           # 读取预测的图片
        img = transform(img)                            # 预处理
        img = torch.unsqueeze(img,dim = 0)              # 增加batch维度

        pred = net(img.to(device))                      # 网络预测

        pred = torch.squeeze(pred)                      # 将(batch、channel)维度去掉
        pred = np.array(pred.data.cpu())                # 保存图片需要转为cpu处理

        pred[pred >=0 ] =255                            # 转为二值图片
        pred[pred < 0 ] =0

        pred = np.uint8(pred)                           # 转为图片的形式
        output_filepath = './result/res.png'
        cv2.imwrite(output_filepath, pred)           # 保存图片
        
    return output_filepath
