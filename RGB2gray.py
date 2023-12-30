from PIL import Image
import os

def convert2gray(input_dir , output_dir):
    #如果输出目录不存在，则创建目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    #获取输入目录的所有文件
    file_list = os.listdir(input_dir)

    #依次处理输入目录的所有文件
    for file_name in file_list:
        #构建完整的输入文件和输出文件路径
        input_path = os.path.join(input_dir , file_name)
        output_path = os.path.join(output_dir , file_name)

        #打开图像并转换为灰度图
        img = Image.open(input_path).convert('L')    #'L'表示灰度图

        #将灰度图保存到输出目录下
        img.save(output_path)

#设置输入和输出目录
input_dir = r'./DRIVE/train/image'
output_dir = r'./DRIVE/train/image'
convert2gray(input_dir , output_dir)

input_dir = r'./DRIVE/test/image'
output_dir = r'./DRIVE/test/image'
convert2gray(input_dir , output_dir)

print("Conversion completed successfully.")
