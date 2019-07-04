# -*- coding: utf-8 -*-
"""
@Date: Created on 2019/6/15
@Author: Haojun Gao
@Description: 
"""


from corpus_seed import corpus_seed
from corpus_split import corpus_split


if __name__ == '__main__':
    data_path = ".\\data"
    rootNode = "0"

    used_word = []

    geo_noun, non_geo_noun, used_word, user_cut = corpus_seed(data_path, rootNode, used_word)

    corpus_split(data_path, geo_noun, user_cut)
