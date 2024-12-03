import pandas
from tqdm import tqdm
from chat_service.lib import cut_sentence
from chat_service.config import config

xiaohuangji_path = r"F:\python_file\Practice\ChatBot\chat_service\prepare_corpus\prepare_classify_corpus\xiaohuangji50w_fenciA.conv"
Q_question_path = r"../QA_get/train_content_answers.txt"
A_question_path = r"../QA_get/train_content_question.txt"


def keyword_in_line(line):
    keywords_list = ["人工智能","python","大数据","c++"]
    for word in line:
        if word in keywords_list:
            return True
        else:
            return False


def process_xiaohuangji(file):
    flag = 0
    for line in tqdm(open(xiaohuangji_path,encoding='utf-8').readlines()):
        #TODO 句子长度为1考虑删除
        if line.startswith("E"):
            flag = 0
            continue
        elif line.startswith("M"):
            if flag == 0:
                line=line[1:].strip()
                flag = 1
            else:
                continue

        line_cuted = cut_sentence.cut(line)
        if not keyword_in_line(line_cuted):
            line_cuted = " ".join(line_cuted)+'\t'+'__label__chat'
            file.write(line_cuted+'\n')


def process():
    f=open(config.classift_corpus_path,"w",encoding='utf-8')
    process_xiaohuangji(f)

    f.close()
