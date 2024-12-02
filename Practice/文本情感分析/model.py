"""
定义模型
"""


import torch.nn as nn
import torch
import lib
from torch.optim import Adam
from dataset import get_dataloader
import torch.nn.functional as F
import os
import numpy as np
from tqdm import tqdm

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel,self).__init__()
        self.embedding = nn.Embedding(len(lib.ws),100)
        self.fc = nn.Linear(lib.max_len*100,2)
        self.lstm = nn.LSTM(input_size=100,
                hidden_size=lib.hidden_size,
                num_layers=lib.num_layers,
                batch_first=True,
                bidirectional=lib.bidriectional,
                dropout=lib.dropout)
        self.fc = nn.Linear(lib.hidden_size*2,2)

    def forward(self, input):
        """

        :param input: [betch_size,max_len]
        :return:
        """
        x = self.embedding(input) #embedding操作，形状：[batch_size,max_len,100]
        #x :[batch_size,max_len,2*hidden_size], h_n :[2*2,batch_size,hidden_size]
        x,(h_n,c_n) = self.lstm(x)
        #获取两个方向最后一次的output，进行concat操作
        output_fw = h_n[-2,:,:] #正向最后一次的输出
        output_bw = h_n[-1,:,:] #反向最后一次的输出
        #最后的output， 【batch_size,hidden_size*2]
        output = torch.cat([output_fw,output_bw],dim=-1)

        out = self.fc(output) #添加一个新的全连接层作为输出层，激活函数处理
        return F.log_softmax(out,dim=-1)


model = MyModel().to(lib.device)
optimizer = Adam(model.parameters(),0.001)
# if os.path.exists("./model/model.pkl"):
#     model.load_state_dict(torch.load("./model/model.pkl"))
#     optimizer.load_state_dict(torch.load("./model/optimizer.pkl"))


def train(epoch):
    for idx,(input,target) in enumerate(get_dataloader(train=True)):
        input = input.to(lib.device)
        target = target.to(lib.device)
        optimizer.zero_grad()
        output = model(input)
        loss = F.nll_loss(output,target)
        loss.backward()
        optimizer.step()
        print(loss.item())

        if idx%100 ==0:
            torch.save(model.state_dict(),"./model/model.pkl")
            torch.save(optimizer.state_dict(),"./model/optimizer.pkl")

def eval():
    loss_list = []
    acc_list = []
    data_loader = get_dataloader(train=False, batch_size=lib.test_batch_size)
    for idx,(input,target) in tqdm(enumerate(data_loader),total = len(data_loader)):
        input = input.to(lib.device)
        target = target.to(lib.device)
        with torch.no_grad():
            output = model(input)
            cur_loss = F.nll_loss(output,target)
            loss_list.append(cur_loss.cpu().item())
            #计算准确率
            pred = output.max(dim=-1)[-1]
            cur_acc = pred.eq(target).float().mean()
            acc_list.append(cur_acc.cpu().item())
    print("total loss,acc:",np.mean(loss_list),np.mean(acc_list))

if __name__ =='__main__':
    # for i in range(1):
    #     train(i)
    eval()