"""
实现把句子转化为数字序列和其反转
"""

class Word2Sequence:
    UNK_TAG = "UNK"
    PAD_TAG = "PAD"

    UNK = 0
    PAD = 1

    def __init__(self):
        self.dict = {
            self.UNK_TAG:self.UNK,
            self.PAD_TAG:self.PAD
        }
        self.count = {}

    def fit(self,sentence):
        """
        把单个句子保存到dict中
        :param sentence: [word1,word2,word3....]
        :return:
        """
        for word in sentence:
            self.count[word] = self.count.get(word,0) + 1


    def __len__(self):
        return len(self.dict)


    def build_vocab(self,min=5,max=None,max_features=None):
        """
        生成词典
        :param min: 最小出现的次数
        :param max: 最大的次数
        :param max_features: 一共保留多少词语
        :return:
        """
        #删除count中词频小于min的word
        if min is not None:
            self.count = {word:value for word,value in self.count.items() if value>min}
        #删除大于max的词
        if max is not None:
            self.count = {word:value for word,value in self.count.items() if value<max}
        #限制保留的词语数
        if max_features is not None:
           temp = sorted(self.count.items(),key=lambda x:x[-1],reverse=True)[:max_features]
           self.count = dict(temp)

        for word in self.count:
            self.dict[word] = len(self.dict)

        #得到一个反转的dict的字典
        self.inverse_dict = dict(zip(self.dict.values(),self.dict.keys()))

        #实现文本转序列
    def transform(self,sentence,max_len=None):
        """
        句子转化序列
        :param self:[word1,word2
        :param sentence:
        :param max_len:int 对句子填充或裁剪
        :return:
        """
        # for word in sentence:
        #     self.dict.get(word,self.UNK)
        if max_len is not None:
            if max_len > len(sentence):
                sentence = sentence + [self.PAD_TAG]*(max_len-len(sentence)) #填充给
            if max_len < len(sentence):
                sentence = sentence[:max_len] #裁剪


        return [self.dict.get(word,self.UNK) for word in sentence]


    def inverse_transform(self,indices):
        """
        靶序列转化为句子
        :param self:
        :param indices:[1,2,3,4,....
        :return:
        """
        return [self.inverse_dict.get(idx) for idx in indices]

#if __name__ == '__main__':
    # ws = Word2Sequence()
    # ws.fit(["我","是","谁"])
    # ws.fit(["我","是","我"])
    # ws.build_vocab(min = 0)
    # print(ws.dict)
    # ret = ws.transform(["我","在","哪"],max_len=10)
    # print(ret)
    # ret = ws.inverse_transform(ret)
    # print(ret)
