
import string
import pattern.vector #for cosine similarity analysis

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

#wellsdocs = Document(wellslist1)
#vernedocs = Document(vernelist1)
#dot(wellsdocs.vector, vernedocs.vector)
#verne1list+verne2list
