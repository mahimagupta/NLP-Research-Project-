import os
import sys 
import json
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

file1_content = open('/Users/mahimagupta/Desktop/hindi.txt','rU')

for line in file1_content:
    line=line.strip()
# print(len(line))

words=word_tokenize(line)
for word in words:
    print(word)

fdist1 = FreqDist(line)
print(fdist1)
fdist1.most_common(20)

fdist2 = FreqDist(word)
print(fdist2)
fdist1.most_common(2)



# prefixes = {

# अ 
# अति
# आ
# परि 
# वि 
# सु 
# स
# स्व
# बे
# अप
# बद 
# सु
# मनो


# }




# matras_suffixes= {
#     1: ["ो","े","ू","ु","ी","ि","ा"],
#     2: ["कर","ाओ","िए","ाई","ाए","ने","नी","ना","ते","ीं","ती","ता","ाँ","ां","ों","ें"],
#     3: ["ाकर","ाइए","ाईं","ाया","ेगी","ेगा","ोगी","ोगे","ाने","ाना","ाते","ाती","ाता","तीं","ाओं","ाएं","ुओं","ुएं","ुआं"],
#     4: ["ाएगी","ाएगा","ाओगी","ाओगे","एंगी","ेंगी","एंगे","ेंगे","ूंगी","ूंगा","ातीं","नाओं","नाएं","ताओं","ताएं","ियाँ","ियों","ियां"],
#     5: ["ाएंगी","ाएंगे","ाऊंगी","ाऊंगा","ाइयाँ","ाइयों","ाइयां"],
# }.decode('utf-8')