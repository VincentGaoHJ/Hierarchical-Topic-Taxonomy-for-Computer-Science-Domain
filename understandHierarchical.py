# -*- coding: utf-8 -*-
"""
@Date: Created on 2019/7/5
@Author: Haojun Gao
@Description: 
"""

import csv

import math
import numpy as np


def read_embeddings():
    embed_dict = {}
    embed_file = "./raw_data/embeddings.txt"

    with open(embed_file, 'r', encoding="UTF-8") as f:
        for line in f:
            temp = line.split(" ")
            if len(temp) != 102:
                continue
            embed_dict[temp[0]] = temp[1:-1]
    return embed_dict


def read_terms(terms_file):
    file_node = []
    with open(terms_file, 'r', encoding="UTF-8") as f:
        for line in f:
            file_node.append(line[:-1])
    return file_node


def calcu_semantic_distence(obj, term, embed_dict):
    if obj in embed_dict and term in embed_dict:
        vec1 = np.array(list(map(eval, embed_dict[obj])))
        vec2 = np.array(list(map(eval, embed_dict[term])))
        distance = np.sqrt(np.sum(np.square(vec1 - vec2)))
        tuple = (distance, term)
    else:
        tuple = (10000, term)
        return False
    return tuple


def read_paper():
    embed_file = "./raw_data/0_200w.csv"
    user_cut = []
    with open(embed_file) as t:
        reader = csv.reader(t)
        for sentence in reader:
            user_cut.append(sentence[0])
    return user_cut


def calcu_cooccurency_n_physics_distence(obj, term, comments):
    total = len(comments)

    dis_list = []
    obj_alone = 0
    term_alone = 0
    cooccurence = 0
    index = 0
    for comm in comments:
        index += 1
        if index % 100000 == 0:
            print("[{} 处理进度] {} / {}".format(term, index, total))
        comm_list = comm.split(" ")
        flag_1 = 0
        flag_2 = 0
        if obj in comm_list:
            flag_1 = 1
            obj_alone += 1
        if term in comm_list:
            flag_2 = 1
            term_alone += 1
        if flag_1 == 1 and flag_2 == 1:
            cooccurence += 1
            position_1 = comm_list.index(obj)
            position_2 = comm_list.index(term)
            dis = np.square(position_1 - position_2)
            dis_list.append(dis)
    dis_mean = np.mean(np.array(dis_list))
    tuple_physics_distence = (dis_mean, term)

    mutual_information = total * cooccurence / (obj_alone * term_alone)
    mutual_information = math.log2(mutual_information)

    tuple_mutual_information = (mutual_information, term)

    return tuple_mutual_information, tuple_physics_distence


if __name__ == '__main__':
    object = "clustering"

    embed_dict = read_embeddings()
    print(embed_dict[object])

    terms_file_small = "./raw_data/concept_ccs_new.txt"
    terms_file_large = "./raw_data/keywords.txt"

    terms_list_small = read_terms(terms_file_small)
    terms_list_large = read_terms(terms_file_large)

    terms_dis = []

    print(terms_list_large)

    # terms_add = ["retrieval", "ir", "information_retrieval_ir", "text_retrieval", "information_retrieval_system"]

    # terms_list.extend(terms_add)

    for term in terms_list_large:
        term_tuple = calcu_semantic_distence(object, term, embed_dict)
        if term_tuple:
            terms_dis.append(term_tuple)

    dis_result = sorted(terms_dis)
    print(dis_result[0:30])

    comment = read_paper()

    mi_list = []
    pd_list = []
    for _, term in dis_result[:30]:
        tuple_mutual_information, tuple_physics_distence = calcu_cooccurency_n_physics_distence(object, term, comment)
        mi_list.append(tuple_mutual_information)
        pd_list.append(tuple_physics_distence)

    mi_result = sorted(mi_list)
    pd_result = sorted(pd_list)

    print("\nsemantic_distence\n")

    for item in dis_result[:30]:
        if item[1] in terms_list_small:
            print(item)
        else:
            print(item, "同义词项")

    print("\nmutual_information\n")

    for item in mi_result:
        if item[1] in terms_list_small:
            print(item)
        else:
            print(item, "同义词项")

    print("\nphysics_distence\n")

    for item in pd_result:
        if item[1] in terms_list_small:
            print(item)
        else:
            print(item, "同义词项")
