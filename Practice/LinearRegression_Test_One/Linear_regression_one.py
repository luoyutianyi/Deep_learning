import torch
import matplotlib.pyplot as plt

learn_rate = 0.01
#1、准备数据
#y=3x+0.8
x = torch.rand([500,1])
y_true = x*3+0.8

#2、模型计算y_predict
w = torch.rand([1,1],requires_grad=True)
b = torch.tensor(0,requires_grad=True,dtype=torch.float32)


#4、循环反向传播，更新参数

for i in range(500):
    # 3、计算loss
    y_predict = torch.matmul(x, w) + b
    loss = (y_true - y_predict).pow(2).mean()

    if w.grad is not None:
        w.grad.data.zero_()
    if b.grad is not None:
        b.grad.data.zero_()

    loss.backward()
    w.data = w.data - learn_rate * w.grad
    b.data = b.data - learn_rate * b.grad

plt.figure(figsize=(20,8))
plt.scatter(x.numpy().reshape(-1),y_true.numpy().reshape(-1))
y_predict = torch.matmul(x,w) + b
plt.plot(x.numpy().reshape(-1),y_predict.detach().numpy().reshape(-1))
plt.show()