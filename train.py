from model import UNet
from dataset import Data_Loader
from metric import dice_coefficient

from torch import optim
import torch.nn as nn
import torch
 
#网络训练模块
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')    #GPU or CPU
print(device)
net = UNet(in_channels=1, num_classes=1)    #加载网络，通道数改为1是灰度图
net.to(device)    #将网络加载到device上
 
#加载训练集
trainset = Data_Loader("./DRIVE/train/image")
train_loader = torch.utils.data.DataLoader(dataset=trainset,batch_size=1,shuffle=True)
len = len(trainset)    #样本总数为 31
 
#加载测试集
testset = Data_Loader("./DRIVE/test/image")
test_loader = torch.utils.data.DataLoader(dataset=testset,batch_size=1)
 
#加载优化器和损失函数
optimizer = optim.RMSprop(net.parameters(), lr=0.00001,weight_decay=1e-8, momentum=0.9)    #定义优化器
criterion = nn.BCEWithLogitsLoss()    #定义损失函数
 
#保存网络参数
save_path = './UNet.pth'    #网络参数的保存路径
best_acc = 0.0    #保存最好的准确率
 
#训练
for epoch in range(20):
 
    net.train()    #训练模式
    running_loss = 0.0
 
    for image,label in train_loader:
 
        optimizer.zero_grad()    #梯度清零
        pred = net(image.to(device))    #前向传播
        ce_loss = criterion(pred, label.to(device))    #计算交叉熵损失
        dice_loss = 1- dice_coefficient(pred, label.to(device))    #计算dice损失
        loss = (ce_loss + dice_loss) / 2.0    #最终损失函数是交叉熵损失和dice损失的平均
        loss.backward()    #反向传播
        optimizer.step()    #梯度下降
 
        running_loss += loss.item()    #计算损失和
 
    net.eval()    #测试模式
    acc = 0.0    #正确率
    total = 0
    with torch.no_grad():
        count = 0
        dice = 0
        for test_image, test_label in test_loader:
 
            outputs = net(test_image.to(device))    #前向传播
 
            outputs[outputs >= 0] = 1    #将预测图片转为二值图片
            outputs[outputs < 0] = 0
 
            #计算预测图片与真实图片像素点一致的精度：acc = 相同的 / 总个数
            acc += (outputs == test_label.to(device)).sum().item() / (test_label.size(2) * test_label.size(3))
            total += test_label.size(0)
            count = count + 1    #统计test_loader中的图片数量
            dice += dice_coefficient(outputs,test_label.to(device))
 
    accurate = acc / total    #计算整个test上面的正确率
    mean_dice = dice / count    #计算整个test上面的平均dice系数
    print('[epoch %d] train_loss: %.3f  test_accuracy: %.3f %% dice: %.3f' %
          (epoch + 1, running_loss/len, accurate*100, mean_dice))
 
    if accurate > best_acc:     #保留最好的精度
        best_acc = accurate
        torch.save(net.state_dict(), save_path)    #保存网络参数