import codecs

f=codecs.open("/Users/mahimagupta/Desktop/hindi.txt", encoding='utf-8')
text=f.read()
# print(text)

words =[]
for each in text:
    tokens = each.split(' ')
    words =  words+tokens
# return words

for i in words:
    print(i.encode('utf-8'))