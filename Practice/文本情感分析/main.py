from word_to_sequence import Word2Sequence
import pickle
import os
from dataset import tokenlize
from tqdm import tqdm

if __name__ == '__main__':
    ws = Word2Sequence()
    path = r"E:\python_file\Practice\文本情感分析\data\train"
    temp_data_path = [os.path.join(path + r"/pos"), os.path.join(path + r"/neg")]
    for data_path in temp_data_path:
        file_paths = [os.path.join(data_path,file_name) for file_name in os.listdir(data_path) if file_name.endswith("txt")]
        for file_path in tqdm(file_paths):
            sentence = tokenlize(open(file_path,encoding='utf-8').read())
            ws.fit(sentence)
    ws.build_vocab(min=10,max_features=20000)
    pickle.dump(ws, open("data/model/ws.pkl", "wb"))
    print(len(ws))