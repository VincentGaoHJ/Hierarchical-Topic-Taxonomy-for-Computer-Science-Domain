# -*- coding: utf-8 -*-
"""
@Date: Created on 2019/7/4
@Author: Haojun Gao
@Description: 
"""

import csv
import nltk

paper_path = './raw_data/papers.txt'
keyword_path = './raw_data/keywords.txt'
result_path = "./raw_data/0.csv"
new_keyword_path = './raw_data/new_keywords.txt'
keyword_set = set()
with open(keyword_path, 'r') as file:
    for linea in file.readlines():
        linea = linea.replace("\n", "")
        keyword_set.add(linea)
print(keyword_set)


keyword_remain = []
i = 0
for keyword in keyword_set:
    i += 1
    tag_tuple = nltk.pos_tag([keyword])
    if tag_tuple[0][1][0] == "N":
        print(tag_tuple)
        keyword_remain.append(tag_tuple[0][0])

with open(new_keyword_path, 'w', newline='') as t:
    writer = csv.writer(t)
    for keyword in keyword_remain:
        writer.writerow([keyword])


list = []
index = 0
with open(paper_path, 'r') as file:
    for linea in file.readlines():
        index = index + 1
        linea = linea.replace("\n", "")
        list.append(linea)


total = len(list)
remain_sentence = []
i = 0
for sentence in list:
    i += 1
    if i % 1000 == 0:
        print("[处理进度：{}/{}]".format(i, total))
    # print(sentence)
    text = nltk.word_tokenize(sentence)
    tag_list = nltk.pos_tag(text)
    remain = []
    for item in tag_list:
        if len(item[0]) <= 1:
            continue
        if item[0] in keyword_remain:
            remain.append(item[0])
            continue
        if item[1][0] == "N":
            remain.append(item[0])

    sente = " ".join(remain)
    if len(sente) != 0:
        remain_sentence.append(sente)


with open(result_path, 'w', newline='') as t:
    writer = csv.writer(t)
    for sentence in remain_sentence:
        writer.writerow([sentence])



