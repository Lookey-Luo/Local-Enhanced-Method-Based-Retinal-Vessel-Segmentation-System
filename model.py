import torch.nn as nn
import torch
import torch.nn.functional as F
 
 
# 搭建unet 网络
class DoubleConv(nn.Module):    # 连续两次卷积
    def __init__(self,in_channels,out_channels):
        super(DoubleConv,self).__init__()
        self.double_conv = nn.Sequential(
 
            nn.Conv2d(in_channels,out_channels,kernel_size=3,padding=1,bias=False),
            nn.BatchNorm2d(out_channels),                           # 用 BN 代替 Dropout
            nn.ReLU(inplace=True),
 
            nn.Conv2d(out_channels,out_channels,kernel_size=3,padding=1,bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True)
        )
 
    def forward(self,x):
        x = self.double_conv(x)
        return x
 
 
class Down(nn.Module):   # 下采样
    def __init__(self,in_channels,out_channels):
        super(Down, self).__init__()
        self.downsampling = nn.Sequential(
            nn.MaxPool2d(kernel_size=2,stride=2),
            DoubleConv(in_channels,out_channels)
        )
 
    def forward(self,x):
        x = self.downsampling(x)
        return x
 
 
class Up(nn.Module):    # 上采样
    def __init__(self, in_channels, out_channels):
        super(Up,self).__init__()
 
        self.upsampling = nn.ConvTranspose2d(in_channels, in_channels // 2, kernel_size=2, stride=2) # 转置卷积
        self.conv = DoubleConv(in_channels, out_channels)
 
    def forward(self, x1, x2):
        x1 = self.upsampling(x1)
 
        diffY = torch.tensor([x2.size()[2] - x1.size()[2]])         # 确保任意size的图像输入
        diffX = torch.tensor([x2.size()[3] - x1.size()[3]])
 
        x1 = F.pad(x1, [diffX // 2, diffX - diffX // 2,
                        diffY // 2, diffY - diffY // 2])
 
        x = torch.cat([x2, x1], dim=1)  # 从channel 通道拼接
        x = self.conv(x)
        return x
 
 
class OutConv(nn.Module):   # 最后一个网络的输出
    def __init__(self, in_channels, num_classes):
        super(OutConv, self).__init__()
        self.conv = nn.Conv2d(in_channels, num_classes, kernel_size=1)
 
    def forward(self, x):
        return self.conv(x)
 
 
class UNet(nn.Module):   # unet 网络
    def __init__(self, in_channels = 1, num_classes = 1):    #这里修改输入输出的通道数
        super(UNet, self).__init__()
        self.in_channels = in_channels
        self.num_classes = num_classes
 
        self.in_conv = DoubleConv(in_channels, 64)
 
        self.down1 = Down(64, 128)
        self.down2 = Down(128, 256)
        self.down3 = Down(256, 512)
        self.down4 = Down(512, 1024)
 
        self.up1 = Up(1024, 512)
        self.up2 = Up(512, 256)
        self.up3 = Up(256, 128)
        self.up4 = Up(128, 64)
 
        self.out_conv = OutConv(64, num_classes)
 
    def forward(self, x):
 
        x1 = self.in_conv(x)
        x2 = self.down1(x1)
        x3 = self.down2(x2)
        x4 = self.down3(x3)
        x5 = self.down4(x4)
 
        x = self.up1(x5, x4)
        x = self.up2(x, x3)
        x = self.up3(x, x2)
        x = self.up4(x, x1)
        x = self.out_conv(x)
 
        return x