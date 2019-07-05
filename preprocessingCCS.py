# -*- coding: utf-8 -*-
"""
@Date: Created on 2019/7/5
@Author: Haojun Gao
@Description: 
"""
import re


def read_temp(temp_file):
    file_node = []
    with open(temp_file, 'r', encoding="UTF-8") as f:
        for line in f:
            file_node.append(line[:-1])
    return file_node


def write_temp(temp_file, items):
    with open(temp_file, "w") as file:
        for item in items:
            file.write(item + '\n')


ccs_file = './raw_data/concept_ccs.txt'
new_file = './raw_data/concept_ccs_new.txt'

concept = read_temp(ccs_file)

modify = set()
for conc in concept:
    item = conc.lower()
    item = re.sub(r'[^a-zA-Z]', '_', item)
    modify.add(item)

write_temp(new_file, modify)
