# -*- coding: utf-8 -*-
import nltk
from nltk.tag import tnt
from nltk.corpus import indian
output = open("tags.txt","w")
data = open("input.txt", "r")
text=data.read()
train_data = indian.tagged_sents('hindi.pos')
tnt_pos_tagger = tnt.TnT()
tnt_pos_tagger.train(train_data)
tagged_words = (tnt_pos_tagger.tag(nltk.word_tokenize(str(text))))

for word in tagged_words:
    t = word
    word = t[0]
    tag = t[1]
    output.write(word)
    output.write(" : ")
    output.write(tag)
    output.write("\n")

# output.write(str(tagged_words).decode("utf-8"))
# print(str(tagged_words).decode("utf-8"))