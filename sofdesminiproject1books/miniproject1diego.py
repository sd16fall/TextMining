#Have all import statements at top
import string

from pattern.vector import Document, cosine_similarity
#www.clips.ua.ac.be/pages/pattern-vector#document for documentation

""" Analyzes the word frequencies in a book downloaded from
    Project Gutenberg """
######################################H.G. Wells Books#################


def get_word_list1(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
        punctuation, and whitespace are stripped away.  The function
        returns a list of the words used in the book as a list.
        All words are converted to lower case.
    """
    f1 = open(file_name,'r')
    #reads each line
    lines1 = f1.readlines()
    # finds start of book, begins at next line after end of header
    whichline1 = 0
    while lines1[whichline1].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
            whichline1 += 1
    lines1 = lines1[whichline1+1:]

    list1 = [] #empty list to put words in


    for line in lines1:
        line.replace('-', ' ') #Matt told me to do this, don't really know why
        for word in line.split():
    # remove punctuation,convert to lowercase, add to empty word list
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            list1.append(word)
    return list1

def get_top_n_words1(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
        occurring words ordered from most to least frequently occurring.

        word_list: a list of words (assumed to all be in lower case with no
                    punctuation
        n: the number of words to return
        returns: a list of n most frequently occurring words ordered from most
                 frequently to least frequentlyoccurring
    """
    word_counter1={} #empty dictionary to add words in
    for word in word_list:
        #if the word is in the word list it adds one to the previous count
        if word in word_counter1:
            word_counter1[word] = word_counter1[word] + 1
            # if its not, then it adds it to the list
        else:
            word_counter1[word] = 1
#empty frequency list
    frequencylist1 = []
#organizing/sorting the list  by placing common words at the top
    for key,value in word_counter1.items():
        frequencylist1.append((value,key))
    frequencylist1.sort(reverse = True)

#setting the range to give you the first n words, and grabbing only the
#words/keys (1th element), and not the frequency value (oth element)
    toplist1=[]
    for i in range(n):
        toplist1.append(frequencylist1[i][1])
    return toplist1

#choose book
bookwords1= get_word_list1('theislandofdoctormoreau.txt')
#pick your n value
topnwords1= get_top_n_words1(bookwords1,100)
#print back top n words
#print 'the island of doctor moreau common words:'
print topnwords1

""" Analyzes the word frequencies in a book downloaded from
    Project Gutenberg """

import string

def get_word_list2(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
        punctuation, and whitespace are stripped away.  The function
        returns a list of the words used in the book as a list.
        All words are converted to lower case.
    """
    f2 = open(file_name,'r')
    lines2 = f2.readlines()
    # finds start of book, begins at next line after end of header
    whichline2 = 0
    while lines2[whichline2].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
            whichline2 += 1
    lines2 = lines2[whichline2+1:]

    list2 = [] #empty list to put words in


    for line in lines2:
        line.replace('-', ' ') #Matt told me to do this, don't really know why
        for word in line.split():
    # remove punctuation,convert to lowercase, and sort into order
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            list2.append(word)
    return list2

def get_top_n_words2(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
        occurring words ordered from most to least frequently occurring.

        word_list: a list of words (assumed to all be in lower case with no
                    punctuation
        n: the number of words to return
        returns: a list of n most frequently occurring words ordered from most
                 frequently to least frequentlyoccurring
    """
    word_counter2={} #empty dictionary to add words in
    for word in word_list:
        if word in word_counter2:
            word_counter2[word] = word_counter2[word] + 1
        else:
            word_counter2[word] = 1

    frequencylist2 = []

    for key,value in word_counter2.items():
        frequencylist2.append((value,key))
    frequencylist2.sort(reverse = True)

    toplist2=[]
    for i in range(n):
        toplist2.append(frequencylist2[i][1])
    return toplist2

bookwords2= get_word_list2('thetimemachine.txt')
topnwords2= get_top_n_words2(bookwords2,100)

print topnwords2

import string

def get_word_list3(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
        punctuation, and whitespace are stripped away.  The function
        returns a list of the words used in the book as a list.
        All words are converted to lower case.
    """
    f3 = open(file_name,'r')
    lines3 = f3.readlines()
    # finds start of book, begins at next line after end of header
    whichline3 = 0
    while lines3[whichline3].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
            whichline3 += 1
    lines3 = lines3[whichline3+1:]

    list3 = [] #empty list to put words in


    for line in lines3:
        line.replace('-', ' ') #Matt told me to do this, don't really know why
        for word in line.split():
    # remove punctuation,convert to lowercase, and sort into order
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            list3.append(word)
    return list3

def get_top_n_words3(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
        occurring words ordered from most to least frequently occurring.

        word_list: a list of words (assumed to all be in lower case with no
                    punctuation
        n: the number of words to return
        returns: a list of n most frequently occurring words ordered from most
                 frequently to least frequentlyoccurring
    """
    word_counter3={} #empty dictionary to add words in
    for word in word_list:
        if word in word_counter3:
            word_counter3[word] = word_counter3[word] + 1
        else:
            word_counter3[word] = 1

    frequencylist3 = []

    for key,value in word_counter3.items():
        frequencylist3.append((value,key))
    frequencylist3.sort(reverse = True)

    toplist3=[]
    for i in range(n):
        toplist3.append(frequencylist3[i][1])
    return toplist3

bookwords3= get_word_list3('thewaroftheworlds.txt')
topnwords3= get_top_n_words3(bookwords3,100)

print topnwords3
#######################################Jules Verne Books###############
import string

def get_word_list4(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
        punctuation, and whitespace are stripped away.  The function
        returns a list of the words used in the book as a list.
        All words are converted to lower case.
    """
    f4 = open(file_name,'r')
    lines4 = f4.readlines()
    # finds start of book, begins at next line after end of header
    whichline4 = 0
    while lines4[whichline4].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
            whichline4 += 1
    lines4 = lines4[whichline4+1:]

    list4 = [] #empty list to put words in


    for line in lines4:
        line.replace('-', ' ') #Matt told me to do this, don't really know why
        for word in line.split():
    # remove punctuation,convert to lowercase, and sort into order
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            list4.append(word)
    return list4

def get_top_n_words4(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
        occurring words ordered from most to least frequently occurring.

        word_list: a list of words (assumed to all be in lower case with no
                    punctuation
        n: the number of words to return
        returns: a list of n most frequently occurring words ordered from most
                 frequently to least frequentlyoccurring
    """
    word_counter4={} #empty dictionary to add words in
    for word in word_list:
        if word in word_counter4:
            word_counter4[word] = word_counter4[word] + 1
        else:
            word_counter4[word] = 1

    frequencylist4 = []

    for key,value in word_counter4.items():
        frequencylist4.append((value,key))
    frequencylist4.sort(reverse = True)

    toplist4=[]
    for i in range(n):
        toplist4.append(frequencylist4[i][1])
    return toplist4

bookwords4= get_word_list4('aroundtheworldin80days.txt')
topnwords4= get_top_n_words4(bookwords4,100)

print topnwords4


""" Analyzes the word frequencies in a book downloaded from
    Project Gutenberg """

import string

def get_word_list5(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
        punctuation, and whitespace are stripped away.  The function
        returns a list of the words used in the book as a list.
        All words are converted to lower case.
    """
    f5 = open(file_name,'r')
    lines5 = f5.readlines()
    # finds start of book, begins at next line after end of header
    whichline5 = 0
    while lines5[whichline5].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
            whichline5 += 1
    lines5 = lines5[whichline5+1:]

    list5 = [] #empty list to put words in


    for line in lines5:
        line.replace('-', ' ') #Matt told me to do this, don't really know why
        for word in line.split():
    # remove punctuation,convert to lowercase, and sort into order
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            list5.append(word)
    return list5

def get_top_n_words5(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
        occurring words ordered from most to least frequently occurring.

        word_list: a list of words (assumed to all be in lower case with no
                    punctuation
        n: the number of words to return
        returns: a list of n most frequently occurring words ordered from most
                 frequently to least frequentlyoccurring
    """
    word_counter5={} #empty dictionary to add words in
    for word in word_list:
        if word in word_counter5:
            word_counter5[word] = word_counter5[word] + 1
        else:
            word_counter5[word] = 1

    frequencylist5 = []

    for key,value in word_counter5.items():
        frequencylist5.append((value,key))
    frequencylist5.sort(reverse = True)

    toplist5=[]
    for i in range(n):
        toplist5.append(frequencylist5[i][1])
    return toplist5

bookwords5= get_word_list5('twentythousandleaguesunderthesea.txt')
topnwords5= get_top_n_words5(bookwords5,100)

print topnwords5

import string

def get_word_list6(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
        punctuation, and whitespace are stripped away.  The function
        returns a list of the words used in the book as a list.
        All words are converted to lower case.
    """
    f6 = open(file_name,'r')
    lines6 = f6.readlines()
    # finds start of book, begins at next line after end of header
    whichline6 = 0
    while lines6[whichline6].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
            whichline6 += 1
    lines6 = lines6[whichline6+1:]

    list6 = [] #empty list to put words in


    for line in lines6:
        line.replace('-', ' ') #Matt told me to do this, don't really know why
        for word in line.split():
    # remove punctuation,convert to lowercase, and sort into order
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            list6.append(word)
    return list6

def get_top_n_words6(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
        occurring words ordered from most to least frequently occurring.

        word_list: a list of words (assumed to all be in lower case with no
                    punctuation
        n: the number of words to return
        returns: a list of n most frequently occurring words ordered from most
                 frequently to least frequentlyoccurring
    """
    word_counter6={} #empty dictionary to add words in
    for word in word_list:
        if word in word_counter6:
            word_counter6[word] = word_counter6[word] + 1
        else:
            word_counter6[word] = 1

    frequencylist6 = []

    for key,value in word_counter6.items():
        frequencylist6.append((value,key))
    frequencylist6.sort(reverse = True)

    toplist6=[]
    for i in range(n):
        toplist6.append(frequencylist6[i][1])
    return toplist6

bookwords6= get_word_list6('ajourneytothecentreoftheearth.txt')
topnwords6= get_top_n_words6(bookwords6,100)

print topnwords6


# simple cosine_similarity implementation to look at text similarity.
#Note that many common "stop words" the, a, and etc are removed
# look at ww.clips.ua.ac.be/pages/pattern-vector#document for documentation on
#why stop words are removed implictly here. settings mentioned are standard if
#not changed
wellsdocs = Document(topnwords1+topnwords2+topnwords3)
#wellsdocs = Document(topnwords5)
vernedocs = Document(topnwords4+topnwords5+topnwords6)
#vernedocs = Document(topnwords6)

print cosine_similarity(wellsdocs.vector, vernedocs.vector)
