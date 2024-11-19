'''
#模型
from torch import nn

class Lr(nn.Module):
    def __init__(self):
        super(Lr,self).__init__() #继承父类init函数
        self.linear = nn.Linear(1,1)
        #self.fcl = nn.Linear(1,1)

    def forward(self,x):
        out = self.linear(x)
        #out = self.fcl(out)
        return out
'''

'''
#实例化模型
model = Lr()
#传入数据
predict = model(x)
'''


'''
#优化器
model.parameters() #获取模型参数信息
optimizer = optim.SGD(model1.parameters(),lr=le-3) #1、实例化
optimizer.zero_grad() #2、梯度置0
loss.backward() #3、计算梯度
optimizer.step() #4、更新参数
'''

'''
#损失函数
1、均方误差
nn.MSELoss() 常用于分类问题
2、交叉熵损失
nn.CrossEntropyLoss() 常用于逻辑回归

使用方法：
model = Lr() #1、实例化模型
criterion = nn.MSELoss() #2、实例化损失函数
optimizer = optim.SGD(model.parameters(),lr = le-3) #3、实例化优化器类
for i in range(100):
    y_predict = model(x_true) #4、向前计算预测值
    loss = criterion(y_true,y_predict) #5、调用损失函数传入真实值和预测值，得到损失结果
    optimizer.zero_grad() #5、当前循环参数梯度置为0
    loss.backward() #6、计算梯度
    optimizer.step() #7、更新参数的值
'''

import torch
import torch.nn as nn
from torch.optim import SGD

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


#0、准备数据

x = torch.rand([500,1]).to(device)
y_true = 3*x + 0.8

#1、定义模型
class MyLinear(nn.Module):
    def __init__(self):
        super(MyLinear,self).__init__()
        self.linear = nn.Linear(1,1)

    def forward(self, x):
        out = self.linear(x)
        return out


#2、实例化模型，优化器类，loss实例化
my_linear = MyLinear().to(device)
optimizer = SGD(my_linear.parameters(),0.001)
loss_fn = nn.MSELoss()

#3、循环，梯度下降，参数更新
for i in range(2000):
    #得到预测值
    y_predict = my_linear(x)
    loss = loss_fn(y_predict,y_true)
    #梯度置为0
    optimizer.zero_grad()
    #反向传播
    loss.backward()
    #参数更新
    optimizer.step()
    params = list(my_linear.parameters())
    print(loss.item(),params[0].item(),params[1].item())