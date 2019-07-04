# -*- coding: utf-8 -*-
"""
@Date: Created on 2019/6/15
@Author: Haojun Gao
@Description: 
"""

import nltk
from collections import Counter
from corpus_seed import generate_sentences, get_classify, find_seed


# 统计词频
def CountWord(comment_sentence):
    """

    :param POI: POI字符串
    :return:
    """
    comment = " ".join(comment_sentence)
    doc = comment.split(' ')
    c = Counter(doc)
    cnt = []
    for k, v in c.items():
        cnt.append((k, v))
    cnt.sort(key=lambda x: x[1], reverse=True)
    return cnt




def corpus_seed(data_path, fileNode, used_word):
    print('\n==========================\n Running Node  ', fileNode, '\n==========================')

    user_cut = generate_sentences(data_path, fileNode)
    print("景点文章：", user_cut[:3])

    sort_Word = CountWord(user_cut)
    print("景点名词：", sort_Word[:10])

    geo_noun, non_geo_noun = get_classify(sort_Word, used_word)
    print("地理名词集合 {}".format(geo_noun))
    print("特征名词集合 {}".format(non_geo_noun))

    # geo_noun = find_seed(user_cut, geo_noun)
    #
    # print("使用过的名词集合 {}".format(used_word))
    #
    # used_word.extend(geo_noun)
    # used_word.extend(non_geo_noun)
    #
    # # 绘制绘图所用格式输出
    # write_output(data_path, geo_noun, non_geo_noun, fileNode)
    #
    # return geo_noun, non_geo_noun, used_word, user_cut


if __name__ == '__main__':
    data_path = ".\\data"
    rootNode = "0"

    used_word = []

    corpus_seed(data_path, rootNode, used_word)

    # count_result = CountWord(list)
    # print(len(count_result))
    # print(count_result[:100])
