import os
from PIL import Image
import numpy as np
import random

source_imgs_dir = './DRIVE/train/image'
source_masks_dir = './DRIVE/train/label'
target_imgs_dir = './DRIVE_patch/train/image'
target_masks_dir = './DRIVE_patch/train/label'

# 确保输出目录存在
if not os.path.exists( target_imgs_dir ):
	os.makedirs( target_imgs_dir )
if not os.path.exists( target_masks_dir  ):
	os.makedirs( target_masks_dir  )

image_size = 512    #每张图像调整为512×512分辨率
patch_size = 64    #每个块的大小是64×64分辨率
patch_number = 200    #每张图像切取200个块

img_idx = 0

for filename in os.listdir( source_imgs_dir ):

	filepath = os.path.join( source_imgs_dir , filename )    #获取输入图像的完整路径
	img = Image.open( filepath )    #打开待分块的输入图像
	img.resize(( image_size , image_size ))    #将输入图像调整为指定分辨率
	masks_filename = filename
	masks_filepath = os.path.join( source_masks_dir , masks_filename )    #获取输入掩码的完整路径
	mask = Image.open( masks_filepath )    #打开待分块的掩码图像
	mask.resize(( image_size , image_size ))    #将输入掩码调整为指定分辨率
	for patch_idx in range( 1 , patch_number + 1 ):
		target_idx = patch_number * img_idx + patch_idx    #为输出图像和掩码生成编号
		target_imgs_filename = str( target_idx ) + '_training.png'
		target_imgs_filepath = os.path.join( target_imgs_dir , target_imgs_filename )    #输出图像待保存地址
		target_masks_filename = str( target_idx ) + '_training.png'
		target_masks_filepath = os.path.join( target_masks_dir , target_masks_filename )    #输出掩码待保存地址
		x = random.randint( 0 , image_size - patch_size )    #随机生成切片位置x坐标
		y = random.randint( 0 , image_size - patch_size )    #随机生成切片位置y坐标
		patch_img = img.crop(( x , y , x + patch_size , y + patch_size ))    #根据x和y坐标裁剪图像
		patch_img.save( target_imgs_filepath )    #保存输出图像块到输出目录
		patch_mask = mask.crop(( x , y , x + patch_size , y + patch_size ))    #根据x和y坐标裁剪掩码
		patch_mask.save( target_masks_filepath )    #保存输出掩码块到输出目录
	img_idx = img_idx + 1

print("Successfully split the training set.")