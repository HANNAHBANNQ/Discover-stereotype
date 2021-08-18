#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 11:14:36 2021

@author: hannahbannq
"""
import gensim.models
from gensim.models.word2vec import Word2Vec
import scipy.stats as stats

#retrieve or establish model
model = gensim.models.word2vec.Word2Vec.load("/Users/hannahbannq/Downloads/Tencent.w2v")
file = '/Users/hannahbannq/Downloads/Tencent_AILab_ChineseEmbedding/Tencent_AILab_ChineseEmbedding.txt'
model = gensim.models.KeyedVectors.load_word2vec_format(file, binary=False)

vocab = model.key_to_index
words = list(vocab.keys())

#load lists
north = ['山东人','河北人','北京人','山西人','天津人','内蒙古人','北方人']
northwest = ['新疆人','宁夏人','甘肃人','陕西人','青海人','西北人']
central = ['湖北人','河南人','中原人']
yangtse = ['江苏人','浙江人','上海人','安徽人']
southwest = ['湖南人','广西人','贵州人','云南人','四川人','重庆人','江西人','西藏人','西南人']
northeast = ['黑龙江人','吉林人','辽宁人','东北人']
south = ['福建人','广东人','海南人','南方人']

#competence & warm
com_H = ['任人唯贤','高效','坚定','上流','优雅','自信','持久','坚决','机智',
        '敏锐','狡猾','公事公办','多才多艺','不屈','精打细算','纪律严明','诡计多端',
        '主导','职业','野心','实际','智慧','能力','强大','世故','坚定自信',
        '竞争力','独立','专业','成功','熟练','精明','教养','强势','性感','勤奋',
        '负责任','富有成效','酷','努力工作','主见','科学','勤劳','断然','积极',
        '想象力','得力','有序','尽职','奋斗','自律','深思熟虑']

com_L = ['固执','情绪化','啰嗦','不可靠','保守','不可信','冒险','无用','懒惰','笨蛋',
       '无力','机会主义','危险','剥削','迟钝','依赖他人','不劳而获','神经质','焦虑','郁闷',
       '浮躁','脆弱','寻求刺激','抱怨']


warm_H = ['简单','直率','爽快','诚实','耿直','礼貌','英勇','节俭','善良',
             '照顾','抚慰','宽容','值得信赖','友好','真诚','品质好',
             '温暖','讨人喜欢','善意','外向','快乐','吸引力','善交际','友好','随和',
             '支持','乐于助人','同情心','享受生活','开放','认真','自觉','合群',
             '积极情绪','利他主义','信任','谦逊','温柔','家长式']

warm_L = ['野蛮','暴脾气','贪婪','不好相处','拉帮结派','讨厌','抱怨','冷酷','贪婪',
            '不诚实','自夸','自负','生气','敌意']

com_h = list(set(com_H))
com_l=list(set(com_L))
warm_h=list(set(warm_H))
warm_l=list(set(warm_L))

#print competence score of each province in the same group

def seperate(group, trait_h, trait_l):
    result = [] 
    result2 = []
    result_ch = []
    result_cl = []
    stereo = []
    for i in range(len(group)):
        for h in trait_h:
            similar_h = model.similarity(group[i],h)
            result.append(similar_h)
        result_ch.append(sum(result)/len(trait_h)) 

        for l in trait_l:
            similar_l = model.similarity(group[i],l)
            result2.append(similar_l)
        result_cl.append(sum(result2)/len(trait_l)) 
    for i in range(len(group)):
        stereo.append(result_ch[i]-result_cl[i])
    return(result_ch, result_cl, stereo)  
 
#seperate(yangtse,com_h,com_l)

def validate_MW(group):
    return(stats.mannwhitneyu(seperate(group,com_h,com_l)[2],seperate(group,warm_h,warm_l)[2],alternative='two-sided'))
#validate(yangtse)

#MW U teset
area =[north, northwest, central, yangtse, southwest, northeast, south]
groupname = ['north', 'northwest', 'central', 'yangtse', 'southwest', 'northeast', 'south']
for i in range(len(groupname)):
    print(groupname[i]+':'+"  "+str(validate_MW(area[i])))

#paired t test:    
def validate_pairedT(group):
    return stats.ttest_rel(seperate(group,com_h,com_l)[2],seperate(group,warm_h,warm_l)[2])
for i in range(len(groupname)):
    print(groupname[i]+':'+"  "+str(validate_pairedT(area[i])))
        
           