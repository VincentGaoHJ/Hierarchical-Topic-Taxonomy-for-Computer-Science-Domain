# -*- coding: utf-8 -*-
"""
@Date: Created on 2019/7/4
@Author: Haojun Gao
@Description: 
"""

import csv

paper_path = './raw_data/papers.txt'
domain = "information_retrieval"
domain_path = "./raw_data/" + domain + ".csv"

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

    if sentence.find("information_retrieval") != -1:
        remain_sentence.append(sentence)


with open(domain_path, 'w', newline='') as t:
    writer = csv.writer(t)
    for sentence in remain_sentence:
        writer.writerow([sentence])
