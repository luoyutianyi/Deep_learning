from prepare_corpus.prepare_user_dict.TryUser_Dict import test_user_dicr
from lib.cut_sentence import cut
from chat_service.lib import stopwords

if __name__ == '__main__':
    #test_user_dicr()
    a = "python是什么啊aaa!!!????"
    print(cut(a,use_stopwords=True))
    #print(stopwords)