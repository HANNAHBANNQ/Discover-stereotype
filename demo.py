#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: hannahbannq
"""
import re
import sys
import numpy as np
import gensim.models
from gensim.models.word2vec import KeyedVectors

huji = ['河北人',
'河南人',
'山西人',
'山东人',
'湖北人',
'湖南人',
'云南人',
'江西人',
'广东人',
'广西人',
'北京人',
'陕西人',
'西藏人',
'内蒙古人',
'甘肃人',
'江苏人',
'安徽人',
'福建人',
'黑龙江人',
'青海人',
'四川人',
'贵州人',
'上海人',
'浙江人',
'海南人',
'新疆人',
'吉林人',
'辽宁人',
'宁夏人',
'天津人',
'重庆人',
'澳门人',
'台湾人',
'香港人'
]

province = ['河北',
'河南',
'山西',
'山东',
'湖北',
'湖南',
'云南',
'江西',
'广东',
'广西',
'北京',
'陕西',
'西藏',
'内蒙古',
'甘肃',
'江苏',
'安徽',
'福建',
'黑龙江',
'青海',
'四川',
'贵州',
'上海',
'浙江',
'海南',
'新疆',
'吉林',
'辽宁',
'宁夏',
'天津',
'重庆',
'澳门',
'台湾',
'香港']

file = '/sgns.sogounews.bigram-char.txt'

model = gensim.models.KeyedVectors.load_word2vec_format(file, binary=False)
# obtain words dictionary
vocab = model.key_to_index
words = list(vocab.keys())

#evaluation using three files
print(model.evaluate_word_analogies(analogies="/Users/hannahbannq/Documents/GitHub/Chinese-Word-Vectors/testsets/CA8/semantic.txt")[0])
print(model.evaluate_word_analogies(analogies='/Users/hannahbannq/Documents/GitHub/Chinese-Word-Vectors/testsets/CA8/morphological.txt')[0])
print(model.evaluate_word_analogies(analogies='/Users/hannahbannq/Documents/GitHub/Chinese-Word-Vectors/testsets/CA_translated/ca_translated.txt')[0])

#bubble sort
#list=filtered，排序时比较的s[i][1]
def bubble_sort(list):
    count = len(list)
    for i in range(count):
        for j in range(i + 1, count):
            if list[i][1] < list[j][1]:
                list[i], list[j] = list[j], list[i]
    return list

#top1000 similar words
filtered_list = []

#filter uninterested words
for target in huji:
    if target in words:
        s = model.most_similar(positive=[target], topn=1000)
        delete1 = []
        for pairs in s:
            if len(pairs[0]) < 3:
                continue
            if pairs[0][0:2] in province or pairs[0][2] == '人' or pairs[0][0:3] in province:
                delete1.append(pairs)
        #elif pairs[0][2] == '人':
            #delete1.append(pairs)
        #elif pairs[0][0:3] in province:
            #delete1.append(pairs)
                       
        filtered = list(set(s).difference(delete1))    
        filtered_list.append(bubble_sort(filtered))
        filtered_list.append('___以上是'+target+'的分割线___')
    else:
        filtered_list.append(target+'is not found in corpus')
    
#save as output
output_list = [] 

for filtered in filtered_list:
    for pair in filtered:
        output = '\n'.join([str(pair)])
        output_list.append(output)
        
#save as a file
fin = open(r'similarity0622.txt','w') 
output_line = '\n'.join([str(x) for x in output_list])
fin.write(str(output_line))
fin.close()

#make up possible words but filtered by previous steps
missing = ['正经人','厚道人','体贴人','老实人','明白人','聪明人']
for miss in missing:
    for ren in huji:
        if ren in words:
            #similar = model.similarity(ren,miss)
            print(ren+'&'+miss+':'+str(model.similarity(ren,miss)))
        else:
            print(ren+'no key found')




