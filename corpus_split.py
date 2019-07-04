# -*- coding: utf-8 -*-
"""
@Date: Created on 2019/6/14
@Author: Haojun Gao
@Description: 
"""

import csv
import os


def corpus_split(data_path, geo_noun, user_cut):
    for sentence in user_cut:
        influPoi = ""
        influZone = []
        word_list = sentence.split(' ')
        # 判断段落中有没有分割词
        res = list(set(geo_noun).intersection(set(word_list)))
        if len(res) == 0:
            continue
        # 有分割词的话
        else:
            # 只有一个分割词，那么这段归这个分割词
            if len(res) == 1:
                # 将这句话划归为出现了的景点
                poi = res[0]
                save_path = os.path.join(data_path, str(poi) + ".csv")
                with open(save_path, 'a+', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([sentence])
            # 如果多于一个分割词，那么就按照势力划分
            else:
                # 遍历每一个词
                for word in word_list:
                    # 如果词不在势力范围内，则加入缓冲区
                    if word not in geo_noun:
                        influZone.append(word)
                    # 如果词在势力范围内，缓冲区内的词归上一次出现的术语
                    else:
                        # 如果之前没有出现过术语，那么缓冲区中的词归这段最早出现的术语
                        if influPoi == "":
                            influPoi = word
                        # print("势力范围共 {} 个词归分割词：{}".format(len(influZone), influPoi))
                        save_path = os.path.join(data_path, str(influPoi) + ".csv")
                        with open(save_path, 'a+', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow([" ".join(influZone)])
                        # 设置下一次缓冲区的归属景点，以及将缓冲区清零
                        influPoi = res[-1]
                        influZone = []

                # 循环完了之后，如果最后几句话存在，且前面有景点出现过，那么这几句话归前面的景点
                if influPoi != "" and influZone != []:
                    save_path = os.path.join(data_path, str(influPoi) + ".csv")
                    with open(save_path, 'a+', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([" ".join(influZone)])


if __name__ == '__main__':
    dirs = ""
    data_path = os.path.join(dirs, "data")
    result_path = os.path.join(data_path, "result.csv")
    used_word = ["中国", "时间", '风景', '景色']
    corpus_split(data_path, "0", used_word)
