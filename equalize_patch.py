from PIL import Image
import os
import cv2

def histogram_equalization(image_path):
    #读取图像
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    #直方图均衡化操作
    equ = cv2.equalizeHist(img)

    #保存均衡化后的图像，覆盖掉均衡化前的图像
    cv2.imwrite(image_path, equ)

def process_images_in_directory(directory_path):
    #读取指定目录下的所有png格式文件
    image_files = [f for f in os.listdir(directory_path) if f.endswith('.png')]

    #对指定目录下的每一个png格式文件做直方图均衡化
    for image_file in image_files:
        image_path = os.path.join(directory_path, image_file)
        histogram_equalization(image_path)

#处理训练集
train_directory = './DRIVE_patch/train/image'
process_images_in_directory(train_directory)

#处理测试集
test_directory = './DRIVE_patch/test/image'
process_images_in_directory(test_directory)
