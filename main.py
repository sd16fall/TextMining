# Text Mining project!
# So my goal is to make a thing that will take any topic, gather some info from Wikipedia,
# and then create a haiku about it.
# Used Think Python example Markov code to make this: http://www.greenteapress.com/thinkpython/code/markov.py

"""So, what's the basic concept behind this?
5-7-5 -- Take a likely word, return the next likely word within the remaining about of
	syllables, etc. until there are 17 syllables total. How does one define a syllable?"""

from pattern.web import *
import sys
import string
from random import *
import operator
import unicodedata

# define globals
word_pairs = []		# possible pairs of words

def create_word_pairs(text_list):
	# fills global word_pairs with possible pairs of words from article
	i = 0
	while i<len(text_list)-1:
		word_pairs.append([text_list[i],text_list[i+1]])
		i+=1

def best_suffix(prefix):
	# takes a word and returns the most likely word to follow it
	# create possible pairs
	possible_suffix = []
	i = 0
	while i<len(word_pairs):
		if prefix == word_pairs[i][0]:
			possible_suffix.append(word_pairs[i][1])
		i+=1
	# create histogram
	word_frequency = dict()
	for word in possible_suffix:
		if word not in word_frequency:
			word_frequency[word] = 1
		else:
			word_frequency[word] += 1
	# sort word_frequency by frequency
	# this is a list of tuples of words and frequencies sorted from low to high by freq
	sorted_frequency = sorted(word_frequency.items(), key=operator.itemgetter(1))
	# this takes the last tuple as the most probable (limits possibilities, but that's ok)
	if len(sorted_frequency)>3:
		index = randint(len(sorted_frequency)-3,len(sorted_frequency)-1) # to prevent word loops
	else:
		index = len(sorted_frequency)-1
	suffix = sorted_frequency[index]
	return suffix[0]


def retrieve_article(your_search):
	# Takes your search and returns the plaintext of the most relevant article
	w = Wikipedia()
	article = w.search(your_search)
	article = article.plaintext(keep=[], replace=blocks, linebreaks=2, indentation=False)
	return article

def generate_haiku(your_search):
	# generates haiku from Wikipedia article using Markov probability
	text = retrieve_article(your_search) # retreive plaintext from wikipedia
	split_text = text.split() # make plaintext into list
	create_word_pairs(split_text) # make wordpairs out of list
	prefix = split_text[randint(0,len(split_text)-1)] # define first word
	line1 = prefix
	line2 = ''
	line3 = ''
	# approximate syllables using average 5 letters per word and 5/3 syllables per word,
	# which is 3 letters/syllable
	while len(line1)<=15:
		prefix = best_suffix(prefix)
		line1 = line1 + ' ' + prefix
	while len(line2)<=21:
		prefix = best_suffix(prefix)
		line2 = line2 + ' ' + prefix
	while len(line3)<=15:
		prefix = best_suffix(prefix)
		line3 = line3 + ' ' + prefix
	print your_search
	print line1
	print line2
	print line3

if __name__ == '__main__':
    #import doctest
    #doctest.testmod()
    generate_haiku('Lie')
    
