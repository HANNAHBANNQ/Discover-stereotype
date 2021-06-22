# Similar-word
The target is finding the most similar words related to characteristics like personality of people from certain provinces in China.
## Chinese word embedding & gensim
This code file includes the process of working out characteristic words of top 1000 similar words as well as similarity > 0.5 with host word. Since normally the top results are words of people from neighbouring provinces which we are not interested in given this project, we first filter them out and then make up the possbile words left due to filtering rule before.
