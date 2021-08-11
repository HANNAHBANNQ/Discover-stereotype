#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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

file = '/Users/hannahbannq/Downloads/Tencent_AILab_ChineseEmbedding/Tencent_AILab_ChineseEmbedding.txt'

model = gensim.models.KeyedVectors.load_word2vec_format(file, binary=False)

# obtain words dictionary
vocab = model.key_to_index
words = list(vocab.keys())

#save and load
model.save("/Users/hannahbannq/Downloads/Tencent.w2v")
model = gensim.models.word2vec.Word2Vec.load("/Users/hannahbannq/Tencent.w2v")

#simple test
model['皖人']
model.similarity('安徽人','皖人')

#bubble sort similarity
def bubble_sort_sim(list):
    count = len(list)
    for i in range(count):
        for j in range(i + 1, count):
            if list[i][1] < list[j][1]:
                list[i], list[j] = list[j], list[i]
    return list

#bubble sort word length
def bubble_sort_len(list):
    count = len(list)
    for i in range(count):
        for j in range(i + 1, count):
            if len(list[i][0]) < len(list[j][0]):
                list[i], list[j] = list[j], list[i]
    return len(list[0][0])


s = model.most_similar(positive=['江苏人'], topn=100)
bubble_sort_len(list(s))

#top1000 similar words & filter out uninterested words
order = []

for target in huji:
    if target in words:
        s = model.most_similar(positive=[target], topn=1000)
        filter1 = []
        i = bubble_sort_len(list(s))
        for pairs in s:
            for num in range(i):
                if len(pairs[0]) == num and pairs[0][num-1] == '人': 
                    filter1.append(pairs)                
        #filtered = list(set(s).difference(delete1))    
        order.append(bubble_sort_sim(list(filter1)))
        order.append('___以上是'+target+'的分割线___')
    else:
        order.append(target+'is not found in corpus')
 
#distinction
order2 = []
for ele in order:
    if ele not in order2:
        order2.append(ele)
    
#order2
    
 
#save as output
output_list = [] 

for group in order2:
    for pair in group:
        output = '\n'.join([str(pair)])
        output_list.append(output)
        
#save as a file
fin = open(r'sim_nofilter.txt','w') 
output_line = '\n'.join([str(x) for x in output_list])
fin.write(str(output_line))
fin.close()