# -*- coding: utf-8 -*-
"""
@Date: Created on Tue Dec 11 13:40:14 2018
@Author: Haojun Gao
@Description: 
"""


def get_set_geo():
    set_geo = set()
    with open("data\\new_keywords.txt", 'r') as file_to_read:
        item = file_to_read.readline()
        while item:
            set_geo.add(item[:-1])
            item = file_to_read.readline()
    return set_geo


def get_classify(user_cut, used_word):
    set_geo = get_set_geo()
    geo_noun = []
    non_geo_noun = []
    for item in user_cut:
        if item[0] in used_word:
            continue
        # if geo_verify(item[0]):
        if item[0] in set_geo:
            geo_noun.append(item[0])
        else:
            non_geo_noun.append(item[0])

    return geo_noun[:10], non_geo_noun[:10]


if __name__ == '__main__':

    used_word = []

    set_geo = get_set_geo()

    list = ['based', 'system', 'model', 'data', 'design', 'method', 'systems', 'information', 'framework', 'applications']

    for i in list:
        if i not in set_geo:
            print(i)

    print(set_geo)
