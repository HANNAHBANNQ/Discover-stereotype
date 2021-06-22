# Similar-word
The target is finding the most similar words related to characteristics such as personality of people from certain provinces in China.
## Chinese word embedding & gensim
This code file includes the process of working out characteristic words from top 1000 similar words. Since normally the top results are words of people from neighbouring provinces which we are not interested in given this project, we first filter them out and then make up the possbile words left due to filtering rule before.
## Requirements
- gensim
## Steps
- create provincial words list
- load embedding & create keywords list
- evaluate embedding performance using test file (https://github.com/Embedding/Chinese-Word-Vectors/tree/master/testsets)
- work out top 1000 similar words and obtain interested word, leave provincial words out
- make up the possbile words left due to filtering rule before
- output
