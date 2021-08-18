# Chinese-similar-word
The target is finding the most similar words related to characteristics such as personality of people from certain provinces in China.
## Requirements
- gensim
## Demo.py
The code file includes the process of working out characteristic words from top 1000 similar words. Since normally the top results are words of people from neighbouring provinces which we are not interested in given this project, we first filter them out and then make up the possbile words left due to filtering rule before.
### Steps
- create provincial words list
- load embedding & create keywords list
- evaluate embedding performance using test file (https://github.com/Embedding/Chinese-Word-Vectors/tree/master/testsets)
- work out top 1000 similar words and obtain interested word, leave provincial words out
- make up the possbile words left due to filtering rule before
- output

## Provincial identity word.py
This file aims at capturing words describing provincial identity and basically shares similar logic with the file #demo#. The final result includes those similar words end with "人".

## Stereotype score.py
This file intends to calculate the stereotype score of each regional group on dimensions - In this file I tried for the dimension of 'competence' for example. 

### Steps
- Preliminary work: see file #demo# and #provincial identity word#. Choose group identity words and dimension words first
- Make sure there is no replication or missing in embedding dictionary
- Calculate average distance, which is average cosine similarity for now
- Calculate stereotype score: distance to high dimension words minus distance to low dimension

## Confirm stereotype
This file intends to validate whether there exists mixed stereotype in different areas. The logic referes to: Fiske S T, Cuddy A J C, Glick P, et al. A model of (often mixed) stereotype content: competence and warmth respectively follow from perceived status and competition[J]. Journal of personality and social psychology, 2002, 82(6): 878.

### Steps
- Calculate the competence and warmth score of provinces inside groups respectively
- For the provinces in each group, test whether the scores in dimensions are significantly different
- This file tries paired t test and Mann Whitney U test
- Infer the stereotype category based on results
