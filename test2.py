# -*- coding: utf-8 -*-
import io
import string
import re
import nltk
from nltk.tag import tnt
from nltk.corpus import indian

f  = open("tech_text_final.txt", "r") 
dataFile  = open("output.txt", "w")
lemmaFile  = open("lemma.txt", "w+")
tagFile = open("tags.txt","w")
wordDict = {}

# Peforms Preprocessing, generates POS Tags for words
def processModel():
    train_data = indian.tagged_sents('hindi.pos')
    tnt_pos_tagger = tnt.TnT()
    tnt_pos_tagger.train(train_data)
    text = f.read()
    test = text.split("।")
    for line in test:
        line=re.sub(r'(\d+)',r' ',line)
        line=line.replace(',',' ')
        line=line.replace('-',' ')
        line=line.replace(':',' ')
        line=line.replace('?',' ')
        line=line.replace('(',' ') 
        line=line.replace(')',' ')
        line=line.replace('.',' ')        
        line = line.split() 
        for word in line:
            if word!=" ":
                tagged_word = (tnt_pos_tagger.tag(nltk.word_tokenize(str(word))))
                dataFile.write(word.rstrip())
                tagFile.write(word.rstrip())
                tagFile.write(" : ")
                tagFile.write(tagged_word[0][1])
                dataFile.write("\n")
                tagFile.write("\n")
    tagFile.close()   
    dataFile.close()
    return        
        

# If a word is tagged as Noun/Preposition/Auxiliary Verb -> The base form remains the same otherwise generate_stem_words function is called
def lemmatize():
    d = open("tags.txt","r")
    data1 = d.read()
    data1 = data1.split("\n")
    data1[-1] = data1[-1].strip('\n')  
      

    for token in data1:
        if token=='':
            continue
        line = token.split(":")
        if line[1].strip().startswith("NN") or line[1].strip().startswith("PR") or line[1].strip().startswith("VAUX") :
            wordDict[line[0].strip()] = [line[0].strip()]

        else:
        
            generate_stem_words(line[0].strip())
    

# Generates Base form based on Suffixes as well as Rules
def generate_stem_words(word):
    
    suffixes = {
    1: ["ो","े","ू","ु","ी","ि","ा"],
    2: ["कर","ाओ","िए","ाई","ाए","ने","नी","ना","ते","ीं","ती","ता","ाँ","ां","ों","ें"],
    3: ["ाकर","ाइए","ाईं","ाया","ेगी","ेगा","ोगी","ोगे","ाने","ाना","ाते","ाती","ाता","तीं","ाओं","ाएं","ुओं","ुएं","ुआं"],
    4: ["ाएगी","ाएगा","ाओगी","ाओगे","एंगी","ेंगी","एंगे","ेंगे","ूंगी","ूंगा","ातीं","नाओं","नाएं","ताओं","ताएं","ियाँ","ियों","ियां"],
    5: ["ाएंगी","ाएंगे","ाऊंगी","ाऊंगा","ाइयाँ","ाइयों","ाइयां"],
        }


    rule1 = suffixes[4][17]
    rule2 = suffixes[4][16]
    rule3 = suffixes[1][1]
    rule4 = suffixes[1][6]
    rule5 = suffixes[1][4]
    rule6 = suffixes[5][4]
    rule7 = suffixes[5][5]
    rule8 = suffixes[5][6]

    
    if word.endswith(rule1):
        wordDict[word] = [word[:word.rindex(rule1)] + suffixes[1][4]]
    
    elif word.endswith(rule2):
        wordDict[word] = [word[:word.rindex(rule2)] + suffixes[1][4]]

    elif word.endswith(rule3):
        wordDict[word] = [word[:word.rindex(rule3)] + suffixes[1][6]]
    
    elif word.endswith(rule4):
        wordDict[word] = [word[:word.rindex(rule4)] + suffixes[1][6]]
    
    elif word.endswith(rule5):
        wordDict[word] = [word[:word.rindex(rule5)] + suffixes[1][4]]
    
    elif word.endswith(rule6):
        wordDict[word] = [word[:word.rindex(rule6)] + suffixes[3][2]]
    
    elif word.endswith(rule7):
        wordDict[word] = [word[:word.rindex(rule7)] + suffixes[3][2]]
    
    elif word.endswith(rule8):
        wordDict[word] = [word[:word.rindex(rule8)] + suffixes[3][2]]
    
    else:
 
        if wordDict.get(word,None) == None:
            wordDict[word] = []
        for key in suffixes.keys():
            for value in suffixes[key]:
                if word.endswith(value):
                    suff = word.rindex(value)
                    wordDict[word].append(word[:suff])

# prints the dictionary with Key as the word and Value as the root word
def printdict():
    for k,v in wordDict.items():
        if not v:
            lemmaFile.write(k + ": "+ k)
        else:
            lemmaFile.write(k + ": ")
            for element in set(v):
                lemmaFile.write(element+" ")
                    
        lemmaFile.write("\n")
     
    

def main():
    
    processModel()
    lemmatize()
    printdict()
    
        
if __name__=="__main__":
    main()