
'''version1# 
Remove words if their similarity with any province is smaller than 0.25 '''
for province in huji:
    for words in trait_copy:
        sim = model.similarity(words,province)
        if sim<0.25:
            trait_copy.remove(words)       

'''version2#
Keep if the similarity of a trait word with 5 (the average number of provinces 
in each group) provinces is > 0.35'''  
new_word = []
for words in trait_pure:
    for province in huji:
        sim = model.similarity(words,province) 
        if sim>0.35: 
            new_word.append(words)
            
new_list = []
for word in new_word:
    if new_word.count(word)>5:
        new_list.append(word)
new_list = list(set(new_list))