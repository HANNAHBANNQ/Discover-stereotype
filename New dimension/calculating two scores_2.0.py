#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 15:34:28 2022

@author: hannahbannq
"""
import gensim.models
from gensim.models.word2vec import Word2Vec
import scipy.stats as stats
from scipy.spatial import distance
import numpy as np
import pandas as pd
from sklearn.preprocessing import normalize
from sklearn.preprocessing import scale
from sklearn import preprocessing
import scipy


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
'重庆人'
]


file = '/Users/hannahbannq/Downloads/Tencent_AILab_ChineseEmbedding/Tencent_AILab_ChineseEmbedding.txt'
model = gensim.models.KeyedVectors.load_word2vec_format(file, binary=False)

#vocab = model.key_to_index
#字典
vocab = model.vocab
#字
words = list(vocab.keys())
#words = list(vocab.keys())

#前N条words
piece = words[0:350000]
#前N条dictionary
model_part = {word:model[word] for word in piece}

stack = []
for word in piece:
  stack.append(model[word])

matrix = np.array(stack)

#normalize when axis=1
#matrix_norm = matrix / matrix.max(axis=1)
matrix_norm = normalize(matrix, axis=1)

#centralize when axis=0
matrix_scaled = scale(matrix_norm)

#链接words & transformed vectors
def find_vector(word):
  index = piece.index(word)
  vector = matrix_scaled[index]
  return vector

######################EU####################
def calculate_eu_province(province,trait):
    scores = []
    for i in range(len(trait)):
        score = distance.euclidean(find_vector(province),find_vector(trait[i]))
        scores.append(score)
    eu = sum(scores)/len(trait)
    return eu

output = pd.read_excel("/Users/hannahbannq/Downloads/scores.xlsx") 
output.set_index(["province"], inplace=True)


##################proactive##################
pro_Aplus = ['进取','积极','上进','奋进','发愤图强','自强','力争上游','奋发向上','自强不息',
            '奋斗','追求','拼搏']
pro_Aminus = ['冒进','追名逐利','好高骛远','抢夺','夺取']
pro_aplus = ['佛系','不争不抢','与世无争','平和','恬淡','无欲无求']
pro_aminus = ['不求上进','不思进取','自暴自弃','故步自封','无所作为','无所事事','惰性','消极']

traits = [pro_Aplus, pro_Aminus, pro_aplus, pro_aminus]
     

###################################fill the form####################################
output = pd.read_excel("/Users/hannahbannq/Downloads/scores.xlsx") 
output.set_index(["province"], inplace=True)


for province in huji:
    for i in range(len(traits)):
        #output['trait'+str(i)] = ''
        output.loc[province,'trait'+str(i)] = calculate_eu_province(province,traits[i])

output.head()

output.to_csv("/Users/hannahbannq/Downloads/scores_eu.csv")

######################cos####################
output = pd.read_excel("/Users/hannahbannq/Downloads/scores.xlsx") 
output.set_index(["province"], inplace=True)

def calculate_cos_province(province,trait):
    scores = []
    for i in range(len(trait)):
        score = model.similarity(province, trait[i])
        scores.append(score)
    cosine = sum(scores)/len(trait)
    return cosine

for province in huji:
    for i in range(len(traits)):
        #output['trait'+str(i)] = ''
        output.loc[province,'trait'+str(i)] = calculate_cos_province(province,traits[i])

output.to_csv("/Users/hannahbannq/Downloads/scores2.csv")
