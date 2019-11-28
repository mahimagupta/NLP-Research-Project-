# -*- coding: utf-8 -*-
import re
# tags = ['NN', 'NST', 'NNP', 'PRP', 'DEM', 'VM', 'VAUX', 'JJ', 'RB', 'PSP', 'RP', 'CC', 'WQ', 'QF', 'QC', 'QO', 'CL', 'INTF', 'INJ', 'NEG', 'UT', 'SYM', 'COMP', 'RDP', 'ECH', 'UNK', 'XC']

tags = ['SYM', 'PRPC', 'CC', 'NNC', 'RP', 'PRP', 'PSP', 'NN', 'JJ', 'NSTC', 'NEG', 'QCC', 'VAUX', 'QC', 'DEM', 'INJ', 'NNPC', 'NNP', 'VM', 'JJC', 'UNK', 'NST', 'QF', 'INTF', 'CCC', 'WQ', 'QO', 'RB', 'RBC', 'QFC', 'RDP']

punctuation = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']


def eliminate(specialchar,word,test_words,pos_tags):
	word = word.strip().split(specialchar)
	for element in word:
		if element!='' and element!=' ':
			test_words.append(element)
			pos_tags.append(-1)
			if element!=word[-1]:
				test_words.append(specialchar)
				pos_tags.append(-1)
	return test_words,pos_tags

def pair(specialchar,word,test_words,pos_tags):
	word=word.strip()
	count = 0
	for element in word:
		if element=='(':
			test_words.append(element)
			pos_tags.append(-1)
			if count!=0:
				test_words.append(word[1:count])
				pos_tags.append(-1)
		
		elif element==')':
			test_words.append(word[1:count])
			pos_tags.append(-1)
			test_words.append(element)
			pos_tags.append(-1)

		count += 1

	return test_words,pos_tags

	
def max_connect(x, y, viterbi_matrix, emission, transmission_matrix):
	max = -99999
	path = -1
	
	for k in xrange(len(tags)):
		val = viterbi_matrix[k][x-1] * transmission_matrix[k][y]
		if val * emission > max:
			max = val
			path = k
	return max, path



def main():

	# Start of Training Phase
	
	start_time = time.time()

	# Path of training files
	filepath = "wordtag_train.txt"
	languages = ["hindi"]
	exclude = ["<s>", "</s>", "START", "END"]
	wordtypes = []
	tagscount = []

	# Open training file to read the contents
	f = codecs.open(filepath, 'r', encoding='utf-8')
	file_contents = f.readlines()

	# Initialize count of each tag to Zero's
	for x in xrange(len(tags)):
		tagscount.append(0)

	# Calculate count of each tag in the training corpus and also the wordtypes in the corpus
	for x in xrange(len(file_contents)):
		line = file_contents.pop(0).strip().split(' ')
		for i, word in enumerate(line):
			if i == 0:
				if word not in wordtypes and word not in exclude:
					wordtypes.append(word)
			else:
				if word in tags and word not in exclude:
					tagscount[tags.index(word)] += 1
	f.close()
	
	# Declare variables for emission and transmission matrix	
	emission_matrix = []
	transmission_matrix = []
		
	# Initialize emission matrix
	for x in xrange(len(tags)):
		emission_matrix.append([])
		for y in xrange(len(wordtypes)):
			emission_matrix[x].append(0)

	# Initialize transmission matrix
	for x in xrange(len(tags)):
		transmission_matrix.append([])
		for y in xrange(len(tags)):
			transmission_matrix[x].append(0)

	# Open training file to update emission and transmission matrix
	#TODO
	f = codecs.open("wordtag_train.txt", 'r', encoding='utf-8')
	file_contents = f.readlines()
	

	# Update emission and transmission matrix with appropriate counts
	row_id = -1
	for x in xrange(len(file_contents)):
		line = file_contents.pop(0).strip().split(' ')
		if line[0] not in exclude:
			col_id = wordtypes.index(line[0])
			prev_row_id = row_id
			row_id = tags.index(line[1])
			emission_matrix[row_id][col_id] += 1
			if prev_row_id != -1:
				transmission_matrix[prev_row_id][row_id] += 1
		else:
			row_id = -1
	
	# Divide each entry in emission matrix by appropriate tag count to store probabilities in each entry instead of just count
	for x in xrange(len(tags)):
		for y in xrange(len(wordtypes)):
			if tagscount[x] != 0:
				emission_matrix[x][y] = float(emission_matrix[x][y]) / tagscount[x]

	# Divide each entry in transmission matrix by appropriate tag count to store probabilities in each entry instead of just count
	for x in xrange(len(tags)):
		for y in xrange(len(tags)):
			if tagscount[x] != 0:
				transmission_matrix[x][y] = float(transmission_matrix[x][y]) / tagscount[x]

	print time.time() - start_time, "seconds for training"

	start_time = time.time()

	# Open the testing file to read test sentences
	#todo
	testpath = "input.txt"
	file_test = codecs.open(testpath, 'r', encoding='utf-8')
	test_input = file_test.readlines()
	
	# Declare variables for test words and pos tags
	test_words = []
	pos_tags = []

	# Create an output file to write the output tags for each sentences
	file_output = codecs.open("input_output.txt", 'w', 'utf-8')
	file_output.close()
	file_output = codecs.open("input_output.txt", 'a', 'utf-8')
	file_output.write("<s> START")
	file_output.write("\n")
	# For each line POS tags are computed
	for j in xrange(len(test_input)):
		
		test_words = []
		pos_tags = []

		line = test_input.pop(0).strip().split(' ')
	
		for word in line:
			test_words.append(word)
			pos_tags.append(-1)

		

		viterbi_matrix = []
		viterbi_path = []
		
		# Initialize viterbi matrix of size |tags| * |no of words in test sentence|
		for x in xrange(len(tags)):
			viterbi_matrix.append([])
			viterbi_path.append([])
			for y in xrange(len(test_words)):
				viterbi_matrix[x].append(0)
				viterbi_path[x].append(0)

		# Update viterbi matrix column wise
		for x in xrange(len(test_words)):
			for y in xrange(len(tags)):
				if test_words[x] in wordtypes:
					word_index = wordtypes.index(test_words[x])
					tag_index = tags.index(tags[y])
					emission = emission_matrix[tag_index][word_index]
				else:
					emission = 0.001

				if x > 0:
					max, viterbi_path[y][x] = max_connect(x, y, viterbi_matrix, emission, transmission_matrix)
				else:
					max = 1
				viterbi_matrix[y][x] = emission * max

		# Identify the max probability in last column i.e. best tag for last word in test sentence
		maxval = -999999
		maxs = -1
		

		for x in xrange(len(tags)):
			if viterbi_matrix[x][len(test_words)-1] > maxval:
				maxval = viterbi_matrix[x][len(test_words)-1]
				maxs = x
			
		# Backtrack and identify best tags for each words
		for x in range(len(test_words)-1, -1, -1):
			pos_tags[x] = maxs
			maxs = viterbi_path[maxs][x]

		
		for i, x in enumerate(pos_tags):
			file_output.write(test_words[i] + " " + tags[x] + " " + "\n")
		file_output.write("</s> END")
		file_output.write("\n")
		file_output.write("<s> START")
		file_output.write("\n")	

	f.close()
	file_output.close()
	file_test.close()

	print time.time() - start_time, "seconds for testing"

if __name__ == "__main__":

	import codecs
	import os
	import sys
	import time
		

	main()
		