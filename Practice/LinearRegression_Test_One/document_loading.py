import torch
from torch.utils.data import Dataset,DataLoader

data_path = r"E:\python_file\Practice\LinearRegression_Test_One\sms+spam+collection\SMSSpamCollection.txt"

#完成数据集类
class MyDataset(Dataset):
    def __init__(self):
        self.lines = open(data_path,encoding = 'mac_roman').readlines()

    def __getitem__(self, index):
        #获取对应位置一条数据
        cur_line = self.lines[index].strip()
        label = cur_line[:4].strip()
        content = cur_line[4:].strip()
        return label, content

    def __len__(self):
        return len(self.lines)

my_dataset = MyDataset()
data_loader = DataLoader(dataset=my_dataset,batch_size=2,shuffle=True) #drop_last=True:截断无法取整的剩余数据

if __name__ == '__main__':
    #my_dataset = MyDataset()

    #print(my_dataset[0])
    #print(len(my_dataset))
    '''
    for i in data_loader:
        print(i)
    '''
    print(len(my_dataset))
    print(len(data_loader))#等于data_set长度除以batch

