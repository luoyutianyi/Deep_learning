"""
存放语料
"""

file_path1 = r"F:\python_file\Practice\ChatBot\chat_service\prepare_corpus\prepare_classify_corpus\xiaohuangji50w_fenciB.conv"
file_path2 = r"F:\python_file\Practice\ChatBot\chat_service\prepare_corpus\prepare_classify_corpus\xiaohuangji50w_fenciA.conv"
f1=open(file_path1,"r",encoding='utf-8')
f2=open(file_path2,"w",encoding='utf-8')
for line in f1.readlines():
    for word in line:
        if word!='/':
            f2.write(word)
f1.close()
f2.close()