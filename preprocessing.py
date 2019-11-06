import os
import sys 
import json
import nltk
import codecs
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
    # print(line)
words=word_tokenize(line)
for word in words:
    print(word)
# print(str(words).strip('[]').decode('utf-8'))

matras= {
    1: ["ो","े","ू","ु","ी","ि","ा"],
    2: ["कर","ाओ","िए","ाई","ाए","ने","नी","ना","ते","ीं","ती","ता","ाँ","ां","ों","ें"],
    3: ["ाकर","ाइए","ाईं","ाया","ेगी","ेगा","ोगी","ोगे","ाने","ाना","ाते","ाती","ाता","तीं","ाओं","ाएं","ुओं","ुएं","ुआं"],
    4: ["ाएगी","ाएगा","ाओगी","ाओगे","एंगी","ेंगी","एंगे","ेंगे","ूंगी","ूंगा","ातीं","नाओं","नाएं","ताओं","ताएं","ियाँ","ियों","ियां"],
    5: ["ाएंगी","ाएंगे","ाऊंगी","ाऊंगा","ाइयाँ","ाइयों","ाइयां"],
}.decode('utf-8')


for m in matras:
    if len(word) > m + 1:
        for mat in matras[m]:
            if word.endswith(mat):
                # return word[:-m]
                #print(word)


# word_freq =[]
# for word in words:
#     word_freq.append(words.count(word))
# print(str(list(zip(words,word_freq))))
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