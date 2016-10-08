import string
import pattern.vector #for cosine similarity analysis

def get_pattern_document(file_name):
    """ comment"""
    f = open(file_name, 'r')
    lines = f.readlines()
    whichline = 0
    while lines[whichline].find('START OF THIS PROJECT GUTENBERG EBOOK') != -1:
        whichline += 1
    lines = lines[whichline+1:]
    book_as_string = " ".join(lines)
    pattern_document = Document(book_as_string)

def get_word_list1(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
        punctuation, and whitespace are stripped away.  The function
        returns a list of the words used in the book as a list.
        All words are converted to lower case.
    """
    f1 = open('theislandofdoctormoreau.txt','r')
    #reads each line
    lines1 = f1.readlines()
    # finds start of book, begins at next line after end of header
    whichline1 = 0
    while lines1[whichline1].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
            whichline1 += 1
    lines1 = lines1[whichline1+1:]

    list1 = [] #empty list to put words in

    document = Document(list1)
