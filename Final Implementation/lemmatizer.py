# -*- coding: utf-8 -*-
import io
import string
import re
import nltk
from nltk.tag import tnt
from nltk.corpus import indian


lemmaFile  = open("lemma.txt", "w+")
outputFile = open('testOutput.txt','w')
wordDict = {}
taggedFile  = open("output_test.txt", "r")

def checkRules():
    rules = []
    with open('rules2.txt','r') as rulesFile:
        for line in rulesFile:
            line = line.strip('\n').split()
            rules.append(line)
    taggedData = []
    prev= ['None']
    for line in taggedFile:
        prevTag = prev.pop(0)
        line= line.strip('\n').split()
        line.append(prevTag)
        currTag = line[1]
        prev.append(currTag)
        taggedData.append(line)
    # print(taggedData)

    count = 0
    for element in taggedData:
        if element[0]=='<s>' or element[0]=='</s>':
            outputFile.write(element[0] + ' ' + element[1])
            outputFile.write('\n')
            continue
        if any(char.isdigit() for char in element[0]) or element[1] == 'SYM':
            outputFile.write(element[0] + ' ' + element[0])
            outputFile.write('\n')
            continue
        flag = 0
        
        for rule in rules:
            if element == rule[:3]:
                count = count+1
                # print('****')
                # print(element)
                # print(rule)
                outputFile.write(element[0] + ' ' + rule[3])
                outputFile.write('\n')
                flag = 1
                # print('****')
                # input()
                break
        if flag == 0:
            lemma = lemmatize(element)
            outputFile.write(element[0] + ' ' + lemma)
            outputFile.write('\n')
        
    print(count)
# If a word is tagged as Noun/Preposition/Auxiliary Verb -> The base form remains the same otherwise generate_stem_words function is called
def lemmatize(element):

        if element[1].strip().startswith("NN") or element[1].strip().startswith("VAUX") :
            return element[0]

        else:
        
            return generate_stem_words(element[0].strip())
    

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
        return word[:word.rindex(rule1)] + suffixes[1][4]
    
    elif word.endswith(rule2):
        return word[:word.rindex(rule2)] + suffixes[1][4]

    elif word.endswith(rule3):
        return word[:word.rindex(rule3)] + suffixes[1][6]
    
    elif word.endswith(rule4):
        return word[:word.rindex(rule4)] + suffixes[1][6]
    
    elif word.endswith(rule5):
        return word[:word.rindex(rule5)] + suffixes[1][4]
    
    elif word.endswith(rule6):
        return word[:word.rindex(rule6)] + suffixes[3][2]
    
    elif word.endswith(rule7):
        return word[:word.rindex(rule7)] + suffixes[3][2]
    
    elif word.endswith(rule8):
        return word[:word.rindex(rule8)] + suffixes[3][2]
    
    else:
        
        for key in suffixes.keys():
            for value in suffixes[key]:
                if word.endswith(value):
                    suff = word.rindex(value)
                    return word[:suff]

    return word
     
    

def main():
    checkRules()
     
        
if __name__=="__main__":
    main()