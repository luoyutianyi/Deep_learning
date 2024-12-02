"""
lstm使用示例

"""

import torch.nn as nn
import torch

batch_size = 10
seq_len = 20 #句子长度
vocab_size = 100 #词典数量
embedding_dim = 30 #用长度为30的向量表示一个词语

hidden_size = 18
num_layer = 1

#构造一个batch的数据
input = torch.randint(low=0,high=100,size=[batch_size,seq_len])


#数据经过embedding处理
embedding = nn.Embedding(vocab_size,embedding_dim)
input_embeded = embedding(input) #[10,20,30]

#把embedding后的数据传入Lstnm
lstm = nn.LSTM(input_size=embedding_dim,hidden_size=hidden_size,num_layers=num_layer,batch_first=True)
output,[h_n,c_n] = lstm(input_embeded)

print(output.size()) #[10,20,18]
print("."*100)
print(h_n.size()) #[1*1,10,18]
print("."*100)
print(c_n.size()) #[1,10,18]

# #获取最后一个时间步上的输出
# last_output = output[:,-1,:]
# #获取最后一次的hidden_state
# last_hidden_state = h_n[-1,:,:]
# print(last_output == last_hidden_state)

last_output = output[:,0,18:]

#反向
last_hidden_state = h_n[-1,:,:]
#1  第一层正向
#-1 第一层反向
#1  第二层正向
#-1 第二层反向

print(last_hidden_state.eq(last_output))

