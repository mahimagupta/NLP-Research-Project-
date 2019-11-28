from sklearn.metrics import accuracy_score
import numpy as np


file1 = "testOutput.txt"
file2 = "testlemma.txt"

with open(file1, 'r') as f:
    data1 = f.readlines()
    data1 = [x.strip() for x in data1]

with open(file2, 'r') as f:
    data2 = f.readlines()
    data2 = [x.strip() for x in data2]

# print(data1)
# print(data2)
# print(len(data1))

count = 0
i = 0
while i<len(data1):
    if data1[i]==data2[i]:
        count = count + 1
    i = i + 1
print(count)

accuracy = accuracy_score(data1, data2)

print(accuracy)






