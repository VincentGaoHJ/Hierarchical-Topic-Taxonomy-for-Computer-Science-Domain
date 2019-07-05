# -*- coding: utf-8 -*-
"""
@Date: Created on 2019/7/5
@Author: Haojun Gao
@Description: 
"""
import json
import re

json_file = './raw_data/SciKG_min_1.0/SciKG_min_1.0.txt'
concept_file = './raw_data/concept.txt'
with open(json_file, 'r', encoding='UTF-8')as file_open:
    data = json.load(file_open)

i = 0
concept = set()
total = len(data)
for index in data:
    i += 1
    if i % 1000 == 0:
        print("[处理进度] {} / {}".format(i, total))
    item = index["name"].lower()
    item = re.sub(r'[^a-zA-Z]', '_', item)
    concept.add(item)
    if item == "performance":

        for expert in index["experts"]:
            print(expert["name"])
            print(expert["interests"])

# with open(concept_file, "w") as file:
#     for conc in concept:
#         file.write(conc + '\n')