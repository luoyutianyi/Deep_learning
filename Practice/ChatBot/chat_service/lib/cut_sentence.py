"""
分词
"""
import string
from chat_service.lib import stopwords
import jieba
import jieba.posseg as psg
from chat_service.config import config
import logging

jieba.setLogLevel(logging.INFO)

jieba.load_userdict(config.user_dict_path)

letters = string.ascii_lowercase+"+"

def cut_sentence_by_word(sentence):
    """实现中英文分词"""
    temp = ""
    result = []
    for word in sentence:
        if word.lower() in letters:
            temp+=word.lower()
        else:
            if temp!="":
                result.append(temp)
                temp=""
            result.append(word.strip())
    if temp!="":
        result.append(temp.lower())
    return result

def cut(sentence,by_word=False,use_stopwords=False,with_sg=False):
    """

    :param sentence: 句子
    :param by_word: 是否按单个字切分
    :param use_stopwords: 是否使用停用词
    :param with_sg: 是否返回词性
    :return:
    """

    #是否单个字
    if by_word:
        result = cut_sentence_by_word(sentence)
    else:
        #是否返回词性
        result = psg.lcut(sentence)
        result = [(i.word,i.flag) for i in result]
        if not with_sg:
            result = [i[0] for i in result]
    #是否使用停用词
    if use_stopwords:
        result = [i for i in result if i not in stopwords]
    return result

if __name__ == "__main__":
    a = "python和c++哪个难aa"
    print(cut_sentence_by_word(a))

