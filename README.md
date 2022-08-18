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
This file intends to validate whether there exists mixed stereotype in different areas. The logic referes to: *Fiske S T, Cuddy A J C, Glick P, et al. A model of (often mixed) stereotype content: competence and warmth respectively follow from perceived status and competition[J]. Journal of personality and social psychology, 2002, 82(6): 878.*

### Steps
- Calculate the competence and warmth score of provinces inside groups respectively
- For the provinces in each group, test whether the scores in dimensions are significantly different
- This file tries paired t test and Mann Whitney U test
- Infer the stereotype category based on results

## Trait words
This file contains two files, one of which is txt file for trait words and the other is the process of doing clustering to the words.

### Steps
- Form the matrix with original word vectors
- Conduct svd to reduce dimensions (the original vector has 200 dimensions)
- Obtain the compressed matrix
- K means: standarization, finding elbow point, k means clustering, comparison of different number of k
- Combine the classes and export to excel

**Update 9/22/2021: filter out words with less frequently-used trait words**   
  
Our target is keep those frequently-used and closely-related words in daily life.First we want to filter out trait words if their similarity with any province is smaller than 
0.35, but unfortunately there is no such word that meets the standard for all provinces.  
  
So I modify the limit of conditions:
- Remove words if their similarity with any province is smaller than 0.25
or,
- Keep if the similarity of a trait word with 5 (the average number of provinces in each group) provinces is > 0.35

**Update 8/18/2022: calculate cosine & euclidean scores per province in the example of "proactive" dimension.**

## New dimension
### Group
We categorize the provinces into three levels in the dimensions of culture (see Chua, R. Y., Huang, K. G., & Jin, M. (2019). ) and wealth (using average of GDP per capita for the recent twenty years)
### Calculating two scores
- Define words that 1) belong to the dimension of "proactive" 2) appear in the pre-trained word embedding 3) belong to the A+, A-, a+, a- separately
- Calculate the similarity of the words and provincial words per dimension and per province, averaged by the count of trait words
- Centralize and normalize the word vectors and calculate the Euclidean distance by the same logic above
### Scores
The results of the *calculating two scores*.
