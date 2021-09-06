#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 15:07:31 2021

@author: hannahbannq
"""
import gensim.models
from gensim.models.word2vec import Word2Vec
import scipy.stats as stats
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

file = 'Tencent_AILab_ChineseEmbedding.txt'
model = gensim.models.KeyedVectors.load_word2vec_format(file, binary=False)

trait_pure=[]
with open("trait_pure.txt", "r") as f: 
    for line in f.readlines():
        line = line.strip('\n')  
        trait_pure.append(line)
trait_pure = list(set(trait_pure)) 

#form the matrix  
matrix = []
for x in trait_pure:
    matrix.append(model[x])
matrix = np.mat(matrix)     

#SVD                  
U,s,V = np.linalg.svd(matrix)      
s  

#determine number of singular value
S_new=[]
def f_process_matric_S(S,Save_information_value):
     """choose the items with large singular value according to the info we want to capture"""
     S_self=0
     N_count=0
     Threshold=sum(s)*float(Save_information_value)
     for value in s:
         if S_self<=Threshold:
             S_new.append(value)
             S_self+=value
             N_count+=1
         else:
             break
     print ("the %d largest singular values keep the %s information " %(N_count,Save_information_value))
     return (N_count,S_new)
 
S_new = f_process_matric_S(s,0.90)

plt.plot(range(200),S_new[1])

#according to elbow point, keep 10 singular values, and obtain compressed matrix
x = np.zeros([556, 200])
V_t = V.T
for i in range(0,10):
    x[i][i]=S_new[1][i]
    
compressed = np.dot(np.dot(U,x),V_t)

#standardization
scaler = StandardScaler()
Com = scaler.fit_transform(compressed)

#choice of number of k
inertia = []
for k in range(1,9):
    kmeans = KMeans(n_clusters=k,random_state=0).fit(Com)
    inertia.append(np.sqrt(kmeans.inertia_))
plt.plot(range(1,9),inertia,'o-')
plt.xlabel('k')
plt.show()

#test k number
kmeans = KMeans(
    init="random",
    n_clusters=4,
    n_init=10,
    max_iter=300,
    random_state=None
    )
kmeans.fit(Com)

#labels
Labels = kmeans.labels_

#classification
class1 = []
class2 = []
class3 = []
class4 = []

for i in range(556):
    if list(Labels)[i] == 0:
        class1.append(trait_pure[i])
    if list(Labels)[i] == 1:
        class2.append(trait_pure[i])
    if list(Labels)[i] == 2:
        class3.append(trait_pure[i]) 
    elif list(Labels)[i] == 3:
        class4.append(trait_pure[i])

print(len(class1),len(class2),len(class3),len(class4))

#combine list
title = ['class1','class2','class3','class4']
classes = [class1, class2, class3, class4]
data_com = [(k, v) for k, l in zip(title, classes) for v in l]

#export to excel
def export_excel(data):
   pf = pd.DataFrame(data)
   #指name
   file_path = pd.ExcelWriter('/lassification_4.xlsx')

   #export
   pf.to_excel(file_path,encoding = 'utf-8',index = False)
   #保存表格
   file_path.save()

export_excel(data_com)

#or we can just put the steps after kmeans into functions:
def kmeans_words(num):
    kmeans = KMeans(
    init="random",
    n_clusters=num,
    n_init=10,
    max_iter=300,
    random_state=None
    )
    kmeans.fit(Com)
    Labels = kmeans.labels_
    return Labels

#num is always greater than n
#under certain k, the words under certain class label
def assign_labels(num,n):
    x = []
    for i in range(len(trait_pure)):
        if kmeans_words(num)[i] == n:
            x.append(trait_pure[i])
    return x

#assign_labels(4,3)
'''
x=[]
for i in range(len(trait_pure)):
    if kmeans_words(4)[i] == 3:
        x.append(trait_pure[i])
'''
#save labels and words accordingly into dictionary
def assign_classes(num):
    data_com = {}
    for i in range(num):
        result = assign_labels(num,i)
        key_string = 'class'+str(i+1)
        data_com[key_string] = result
    return data_com

#assign_classes(4)
 
#set up list of class in preparation for output    
def combin_title(num):
    title = []
    for i in range(num):
        class_title = 'class'+str(i+1)
        title.append(class_title)
    return title

def combin_class(num):
    classes = []
    for i in range(num):
        class_words = assign_classes(num)[combin_title(num)[i]]
        classes.append(class_words)
    return classes
combin_class(4)

def save_excel(num):
    data_com = [(k, v) for k, l in zip(combin_title(num), combin_class(num)) for v in l]
    pf = pd.DataFrame(data_com)
    file_path = pd.ExcelWriter('/Users/hannahbannq/Downloads/classification_'+str(num)+'.xlsx')
    pf.to_excel(file_path,encoding = 'utf-8',index = False)
 
    file_path.save()
