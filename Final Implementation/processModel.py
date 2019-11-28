
# -*- coding: utf-8 -*-
inputFile = open('train.conllu','r')

ruleFile = open('rules.txt','w')
prev =['None']
lineArray = []
for line in inputFile:
    
    if line.find('#')!=-1:
        continue
    elif line.strip('\n')!='':
        line = line.split()

        if line[1]=='।':
            prev = ['None']

        elif line[4]=='SYM' or any(char.isdigit() for char in line[1]):
            prevTag = prev.pop(0)
            currTag = line[4]
            prev.append(currTag)
        else:
            prevTag = prev.pop(0)
            element = line[1] + ' ' + line[4] + ' ' +prevTag +' '+ line[2]
            currTag = line[4]
            prev.append(currTag)
            
            if element in lineArray:
                continue
            lineArray.append(element)
            ruleFile.write(element)
            ruleFile.write('\n')
            
            
        