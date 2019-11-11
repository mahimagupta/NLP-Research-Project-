# -*- coding: utf-8 -*-
import io
import string
import re
f  = open("input.txt", "r") 
    
dataFile  = open("output.txt", "w")
lemmaFile  = open("lemma.txt", "w+")
wordDict = {}
def processModel():
    
    text = f.read()
    test = text.split("।")
    for line in test:
        line=re.sub(r'(\d+)',r' ',line)
        line=line.replace(',',' ')
        line=line.replace('-',' ')
        line=line.replace(':',' ')
        line=line.replace('?',' ')       
        line = line.split()         
        for word in line:
            if word!=" ":
            
                dataFile.write(word.rstrip())
                dataFile.write("\n")
    dataFile.close()
    return 
            
def lemmatize():
    
    mFile  = open("output.txt", "r")
    data = mFile.read()
    data = data.split("\n")
    for word in data:
        
        generate_stem_words(word)
    

def generate_stem_words(word):
   
    suffixes = {
    1: ["ो","े","ू","ु","ी","ि","ा"],
    2: ["कर","ाओ","िए","ाई","ाए","ने","नी","ना","ते","ीं","ती","ता","ाँ","ां","ों","ें"],
    3:["ाकर","ाइए","ाईं","ाया","ेगी","ेगा","ोगी","ोगे","ाने","ाना","ाते","ाती","ाता","तीं","ाओं","ाएं","ुओं","ुएं","ुआं"],
    4: ["ाएगी","ाएगा","ाओगी","ाओगे","एंगी","ेंगी","एंगे","ेंगे","ूंगी","ूंगा","ातीं","नाओं","नाएं","ताओं","ताएं","ियाँ","ियों","ियां"],
    5: ["ाएंगी","ाएंगे","ाऊंगी","ाऊंगा","ाइयाँ","ाइयों","ाइयां"],
        }
 
    if wordDict.get(word,None) == None:
         wordDict[word] = []
    # flag=0
    for key in suffixes.keys():
        for value in suffixes[key]:
            if word.endswith(value):
                suff = word.rindex(value)
                # flag=1
                wordDict[word].append(word[:suff])
                # wordDict[word].append(value)
                # break
        # if(flag==1):
            # break     

def printdict():
    for k,v in wordDict.items():
        # lemmaFile.write(k)
        # lemmaFile.write("\n")
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
    
    
    # lemmatize(dataFile)

     

        
if __name__=="__main__":
    main()