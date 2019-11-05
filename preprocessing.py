import os
import sys 
import json
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist


# with open('/Users/mahimagupta/Desktop/hindi.txt', mode='r+') as fp:
#     for line in fp:
#         words=line.strip('\t\n\r').split(" ")
#         print(words)


# filename=sys.argv[1]
# output_file = "output.txt"
file1_content = open('/Users/mahimagupta/Desktop/hindi.txt','rU')
for line in file1_content:
    line=line.strip()
    print(line)
# words=word_tokenize(line)
# print(words)
# freq=FreqDist(words)
# print(freq)
# file2_content=open('/Users/mahimagupta/Desktop/Hindi Stopwords.txt','rU')
#  print(file2_content)
# for line in file2_content:
#     line=line.strip()
#     print(line)
# file1_content=open('/Users/mahimagupta/Desktop/hindi.txt', encoding='utf8')
# for line in file1_content:
#     line=line.strip()
#     print(line)

# file2_content = open('/Users/mahimagupta/Desktop/Hindi Stopwords.txt','rU')
# tokenized_text=sent_tokenize(file1_content)
# print(tokenized_text)
# tokenized_word=word_tokenize(file1_content)
# print(tokenized_word)
# fdist=FreqDist(tokenized_word)
# print(fdist)
# fdist.most_common(5)
# removed_stopwords =[]
# for w in tokenized_word:
#     if w not in file2_content:
#         removed_stopwords.append(w)
# print(removed_stopwords)







# with open(output_file, mode='w+') as fp:
#     fp.write(json.dumps(0))