# -*- coding: utf-8 -*- 

import os
import sys 
import json
import nltk
import re
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist


class Lemmatize():

	def __init__(self,text=None):
		if text is  not None:
			self.text=text.decode('utf-8')


file1_content = open('/Users/mahimagupta/Desktop/article.txt','rU')

for line in file1_content:
    line=line.strip()
    print(line)

line=re.sub(r'(\d+)',r'',line)
line=line.replace(',','')
line=line.replace('-','')
line=line.replace(':','')
line=line.replace('?','')

words=word_tokenize(line)
for word in words:
    print(word)

# word=re.sub(r'(\d+)',r'',word)
# word=word.replace(',','')
# word=word.replace('-','')
# word=word.replace(':','')
# word=word.replace('?','')


def stemming(self,word):
    suffixes = {
    1: ["ो","े","ू","ु","ी","ि","ा"],
    2: ["कर","ाओ","िए","ाई","ाए","ने","नी","ना","ते","ीं","ती","ता","ाँ","ां","ों","ें"],
    3: ["ाकर","ाइए","ाईं","ाया","ेगी","ेगा","ोगी","ोगे","ाने","ाना","ाते","ाती","ाता","तीं","ाओं","ाएं","ुओं","ुएं","ुआं"],
    4: ["ाएगी","ाएगा","ाओगी","ाओगे","एंगी","ेंगी","एंगे","ेंगे","ूंगी","ूंगा","ातीं","नाओं","नाएं","ताओं","ताएं","ियाँ","ियों","ियां"],
    5: ["ाएंगी","ाएंगे","ाऊंगी","ाऊंगा","ाइयाँ","ाइयों","ाइयां"],
    }

    for s in 5, 4, 3, 2, 1:
        if len(word) > s + 1:
            for suf in suffixes[s]:
                #print type(suf),type(word),word,suf
                if word.endswith(suf):
                    #print 'h'
                    return word[:-s]
    return word

#stopwords
# file2_content=open('/Users/mahimagupta/Desktop/stopwords.txt','rU'')





# fdist1 = FreqDist(line)
# print(fdist1)
# fdist1.most_common(20)

# fdist2 = FreqDist(word)
# print(fdist2)
# fdist1.most_common(2)
