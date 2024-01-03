import numpy as np
import torch
import cv2
from model import UNet
from torchvision import transforms
from PIL import Image
 
transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,),(0.5))
    ])
 
image_size = 512    #每张图像调整为512×512分辨率
patch_size = 256    #每个块的大小是256×256分辨率
dist = 235    #与中心像素点距离超过dist被认为是不感兴趣区域
center_x = image_size // 2
center_y = image_size // 2

#加载模型
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

net = UNet(in_channels=1, num_classes=1)
net.load_state_dict(torch.load('UNet_equalized_patch_256_50.pth', map_location=device))
net.to(device)
 
#测试模式
net.eval()

#分割patch
def segment_one_patch( img ):
    with torch.no_grad():
        img = transform( img )    #预处理
        img = torch.unsqueeze( img , dim = 0)    #增加batch维度
        pred = net(img.to(device))    #网络预测
        pred = torch.squeeze( pred )    #将(batch、channel)维度去掉
        pred = np.array(pred.data.cpu())    #保存图片需要转为cpu处理

        pred[pred >=0 ] =255    #转为二值图片
        pred[pred < 0 ] =0

    return pred

source_img = Image.open('./predict/img.png').convert("L")    #读取预测的图片
source_img.resize(( image_size , image_size ))    #将输入图像调整为指定分辨率
mask = np.zeros(( image_size , image_size ))    #初始化输出掩码
sample_time = image_size//patch_size    #沿每个轴的采样次数

for x_idx in range( sample_time ):
    x = x_idx * patch_size
    for y_idx in range( sample_time ):
        y = y_idx * patch_size
        patch_img = source_img.crop(( x , y , x + patch_size , y + patch_size ))    #根据x和y坐标裁剪图像
        patch_pred = segment_one_patch( patch_img )
        mask[ y : y + patch_size , x : x + patch_size ] = patch_pred

for x_m in range( image_size ):
    for y_m in range( image_size ):
        d = (( x_m - center_x )**2 + ( y_m - center_y )**2)**( 1/2 )
        if d > dist:
            mask[ x_m , y_m ] = 0

mask = np.uint8( mask )    #转为图片的形式
cv2.imwrite('./result/res.png', mask )    #保存图片

