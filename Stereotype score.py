#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 14:10:58 2021

@author: hannahbannq
"""
import gensim.models

#retrieve model
model = gensim.models.word2vec.Word2Vec.load("/Users/hannahbannq/Tencent.w2v")
vocab = model.key_to_index
words = list(vocab.keys())

#list dimension and group words
#for now, we try northern for group A and dimension of competence
northern = ['山东人','河北人','北京人','山西人','天津人','内蒙古人','北方人']
High = ['任人唯贤','高效','坚定','上流','优雅','自信','持久','坚决','机智',
        '敏锐','狡猾','公事公办','多才多艺','不屈','精打细算','纪律严明','诡计多端',
        '主导','职业','野心','实际','智慧','能力','强大','世故','坚定自信',
        '竞争力','独立','专业','成功','熟练','精明','教养','强势','性感','勤奋',
        '负责任','富有成效','酷','努力工作','主见','科学','勤劳','断然','积极',
        '想象力','得力','有序','尽职','奋斗','自律','深思熟虑']

Low = ['固执','情绪化','啰嗦','不可靠','保守','不可信','冒险','无用','懒惰','笨蛋',
       '无力','机会主义','危险','剥削','迟钝','依赖他人','不劳而获','神经质','焦虑','郁闷',
       '浮躁','脆弱','寻求刺激','抱怨']

#remove duplication
high_pure = list(set(High))
low_pure = list(set(Low))

#check whether the word is in the corpus to adjust the words
def check(traits):
    for com in traits:
        if com not in words:
            print(com+'not found')

check(high_pure)
check(low_pure)

#calculating cosine distance
def cos_distance(groupA,trait): 
    distance = []
    for i in groupA:
        for j in trait:
            similarity = model.similarity(i,j)
            distance.append(similarity)
    return(sum(distance)/len(distance))

#calculating stereotype score
def stereo(groupA,trait_H,trait_L):
    comp_h = cos_distance(groupA, trait_H)
    comp_l = cos_distance(groupA, trait_L)
    return(comp_h-comp_l)
stereo(northern,high_pure,low_pure)

#expand to other groups
northern = ['山东人','河北人','北京人','山西人','天津人','内蒙古人','北方人']
northwest = ['新疆人','宁夏人','甘肃人','陕西人','青海人','西北人']
central = ['湖北人','河南人','中原人']
yangtse = ['江苏人','浙江人','上海人','安徽人']
southwestern = ['湖南人','广西人','贵州人','云南人','四川人','重庆人','江西人','西藏人','西南人']
northeastern = ['黑龙江人','吉林人','辽宁人','东北人']
south = ['福建人','广东人','海南人','南方人']

group =[northern, northwest, central, yangtse, southwestern, northeastern, south]
groupname = ['northern', 'northwest', 'central', 'yangtse', 'southwestern', 'northeastern', 'south']
for area in group:
    print(groupname[group.index(area)]+" group's stereotype score for competence is"+"   "+str('%.4f' %stereo(area,high_pure,low_pure)))
