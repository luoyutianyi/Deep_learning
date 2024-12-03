from prepare_corpus.prepare_user_dict.TryUser_Dict import test_user_dicr
from lib.cut_sentence import cut
from chat_service.lib import stopwords
from chat_service.prepare_corpus.QA_get.Json_to_txt import json_to_txt

if __name__ == '__main__':
    #test_user_dicr()
    # a = "python是什么啊aaa!!!????"
    # print(cut(a,use_stopwords=True))
    #print(stopwords)
    json_to_txt()