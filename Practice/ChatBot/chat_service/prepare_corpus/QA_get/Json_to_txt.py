import json

#打开json文件
with open('./cmrc2018_train.json',encoding='utf-8') as fp:
    pyth_list = json.load(fp)
file1 = open("./train_content_question.txt","w",encoding='utf-8')
file2 = open("./train_content_answers.txt","w",encoding='utf-8')

'''
获取完成一条数据
print(pyth_list.get('data')[0].get('paragraphs')[0].get('qas')[0].get('question'))
'''

for i in range(len(pyth_list.get('data'))):
    for j in range(len(pyth_list.get('data')[i].get('paragraphs')[0].get('qas'))):
        question = pyth_list.get('data')[i].get('paragraphs')[0].get('qas')[j].get('question')
        answers = pyth_list.get('data')[i].get('paragraphs')[0].get('qas')[j].get('answers')[0].get('text')
        if(answers == None):
            break
        file1.write(question)
        file1.write('\n')
        file2.write(answers)
        file2.write('\n')
        j=j+1
    i=i+1
    #获取value并保存
