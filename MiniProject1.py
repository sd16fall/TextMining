# Kimber's file
from pattern.en import *
rhymeWords=dict() #dictionary of words that rhyme
generalWords=dict() #markov chain dictionary
#fo = open("ShakespeareSonnets.txt", "r")
with open('ShakespeareSonnets.txt', 'r') as f:
	read_data = f.read()
f.closed
sonnetz= read_data.split('\n\n')
sonnetLine=[0, 1, 2, 3,4, 5,6 ,7, 8, 9, 10, 11, 12, 13]
import random

for k in range(0,len(sonnetz)-1):
	lines=sonnetz[k].split('\n') #splits into lines

	def DictRhymes():
		getRhyme(0, 2) #English sonnet rhyme scheme (lines that rhyme)
		getRhyme(1, 3)
		getRhyme(4, 6)
		getRhyme(5, 7)
		getRhyme(8,10)
		getRhyme(9,11)


	def getRhyme(num1, num2): #num1 and num2 inputs represent which lines are selected (rhyming lines)
		lastword1=lines[num1].split(' ')[-1] #takes the last word of every other line
		lastword2=lines[num2].split(' ')[-1]
		if(sentiment(lastword1)[0]<=.25 and sentiment(lastword2)[0]<=.25):
			if lastword1 in rhymeWords: #checks for existing list
				rhymeWords[lastword1].append(''.join(lastword2)) #extends list if need be
			else:
				rhymeWords[''.join(lastword1)]=[''.join(lastword2)] #otherwise makes a new list
			if lastword2 in rhymeWords:
				rhymeWords[lastword2].append(''.join(lastword1))
			else:
				rhymeWords[lastword2]=[lastword1]

	DictRhymes()

	def getMarkov(): #backwards Markov b/c the end of the line is selected first
		for i in range(0,12):
			getMarkLine(i)

	def getMarkLine(num1): #num1 is the line that is getting processed
		splitLine=lines[num1].split(' ')
		for i in range (1, len(splitLine)):
			curWord= splitLine[-i]
			prevWord=splitLine[-i-1]
			if(sentiment(curWord)[0]<=.25):
				if curWord in generalWords: #checks for existing list
					generalWords[curWord].append(''.join(prevWord)) #extends list if need be
				else:
					generalWords[''.join(curWord)]=[''.join(prevWord)] #otherwise makes a new list

	getMarkov()



def genLine(line1, line2):
	startLine1=random.choice(rhymeWords.keys()) #picks a random rhyming word**'
	startLine2=rhymeWords[startLine1][random.randint(0,len(rhymeWords[startLine1])-1)] #picks a random rhyme to rhyme with the first rhyme
	curWord1=startLine1 #current word processed line 1
	curWord2=startLine2 #current word processed line 2

	for i in range (0,8):
		if curWord1 in generalWords:
			rando1=random.randint(0,len(generalWords[curWord1])-1)
			prevWord1 = generalWords[curWord1][rando1] #picking a word randomly from the list in the dictionary to go with the first one
		else:
			prevWord1=random.choice(generalWords.keys())

		if curWord2 in generalWords:
			rando2=random.randint(0,len(generalWords[curWord2])-1)
			prevWord2=generalWords[curWord2][rando2] 
		else:
			prevWord2=random.choice(generalWords.keys())
		curWord1=prevWord1 #resetting
		curWord2=prevWord2
		startLine1= prevWord1+ ' '+ startLine1 #adding the previous word to the new one.
		startLine2= prevWord2+ ' '+ startLine2
	sonnetLine[line1]=startLine1
	sonnetLine[line2]=startLine2

def genSonnet(): ##generating these lines and putting them into a list
	genLine(0,2)
	genLine(1,3)
	genLine(4,6)
	genLine(5,7)
	genLine(8, 10)
	genLine(9, 11)
	genLine(12, 13)

genSonnet()
print '***************************************************************************'
for i in range (0,14):
	print sonnetLine[i] #printing out the list of lines <3 :D