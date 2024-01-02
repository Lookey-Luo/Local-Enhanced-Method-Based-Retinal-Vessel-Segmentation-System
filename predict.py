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
 
 
# 加载模型
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
net = UNet(in_channels=1, num_classes=1)
net.load_state_dict(torch.load('UNet.pth', map_location=device))
net.to(device)
 
# 测试模式
net.eval()
with torch.no_grad():
 
    img = Image.open('./predict/img.png')           # 读取预测的图片
    img = transform(img)                            # 预处理
    img = torch.unsqueeze(img,dim = 0)              # 增加batch维度
 
    pred = net(img.to(device))                      # 网络预测
 
    pred = torch.squeeze(pred)                      # 将(batch、channel)维度去掉
    pred = np.array(pred.data.cpu())                # 保存图片需要转为cpu处理
 
    pred[pred >=0 ] =255                            # 转为二值图片
    pred[pred < 0 ] =0
 
    pred = np.uint8(pred)                           # 转为图片的形式
    cv2.imwrite('./result/res.png', pred)           # 保存图片