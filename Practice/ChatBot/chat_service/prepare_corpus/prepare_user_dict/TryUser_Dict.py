"""
测试用户词典
"""

import jieba
from chat_service.config import config

jieba.load_userdict(config.user_dict_path)

def test_user_dicr():
    sentence = "人工智能+python和c++哪个难"
    ret = jieba._lcut(sentence)
    print(ret)