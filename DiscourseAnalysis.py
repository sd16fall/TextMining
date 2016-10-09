from pattern.en import sentiment, modality

def replace_all(text, dic): #Looks at text and replaces all occurances of each key in dic with the given value
    for key, value in dic.iteritems(): #Iterates through all the keys and values of dic
        text = text.replace(key, value) #replaces key with value in text
    return text

def sort_data(data): #Takes a CSV file for a transcript (assumes names are in the first column and speech in the second) and outputs the data sorted into a dictionary with the names as keys and everything the individual says as the value.
    fin = open(data) #Opens the specified file
    d = {} #Creates empty dictionary that data will be sorted into
    bad_text = {"\x92": "'", "\x85": "'", "\r": "", "\n": "'"} #Dictionary of codes for formatting and characters that do not carry over into a CSV file. Values associated with each key will replace the "bad" characters
    for line in fin:
        text = replace_all(line, bad_text) #Uses the replace all function to remove characters in bad_text and replace them with their associated values
        key = text[0:text.index(',')].lower().strip() #Creates the keys for the sorted dictionary. Takes the characters from the beginning of each line to the first comma to get just the name in the first column.
        if key in d: #if the key is already in the dictionary, the text is appended to the associated name in the dictionary
            d[key].append(text[text.index(',')+1:])
        else:
            d[key] = [text[text.index(','):]] #If the key has not been added to the dictionary yet it adds the name and the associated text on that line
    return d

def get_sentiment(d): #Takes a dictionary and returns a new dictionary of values for sentiment for every line in the original dictionary
    #The sentiment function returns two values in a list. The first rates the polarity of a sentence (positive or negative) from -1.0 to 1.0, where postive correlates with positive language. The second value is the subjectivity of a sentence from 0.0 to 1.0, where sujective language scores a 1.0.
    sent = {}
    for key, value in d.items():
        sent[key] = [] #Creates an empty list for each key in the dictionary
        for x in value:
            sent[key].append(sentiment(x)) #Adds the sentiment rating for each line in the transcript for each key
    return sent

def get_modality(d): #Takes a dictionary and creates a new dictionary of values for modality for every line in the original dictionary.
    #Modality is a rating of how certain somebody is on a range from -1.0 to 1.0, where negative values indicate uncertainty and positive values represent certainty. Values greater than 0.5 represent facts.
    mod = {}
    for key, value in d.items():
        mod[key] = [] #Creates an empty list for each key in the dictionary
        for x in value:
            mod[key].append(modality(x)) #Adds the sentiment rating for each line in the transcript for each key
    return mod

def average_modality(data): #Takes a dictionary, calculates the average modality for each value, and stores it with the same key
    mod = get_modality(data)
    avg = {}
    for key, value in mod.items():
        summation = 0 #Initializes the sum of the modality rating for each line
        total = 0 #Initializes a counter for the total number of lines for a given person
        avg[key] = [] #Creates an empty list to store each result
        for x in value:
            summation += x #Adds the modality data to the value
            total += 1 #Increments the total number by 1 to represent the total number of spoken lines
        avg[key].append(summation/total) #Divides the sum by the total to provide an average modality for each person
    return avg

def average_polarity(data): #Takes a dictionary, calculates the average polarity for each value, and stores it with the same key
    sent = get_sentiment(data)
    avg = {}
    for key, value in sent.items():
        summation = 0 #Initializes the sum of the polarity rating for each line
        total = 0 #Initializes a counter for the total number of lines for a given person
        avg[key] = []
        for x in value:
            summation += x[0] #Adds the polarity data to the value. The sentiment function returns a list with polarity in the 0th position
            total += 1 #Increments the total number by 1 to represent the total number of spoken lines
        avg[key].append(summation/total) #Divides the sum by the total to provide an average polarity for each person
    return avg

def average_subjectivity(data): #Takes a CSV transcript (assumes names are in the first column and speech in the second) and returns the average subjectivity for each person
    sent = get_sentiment(data)
    avg = {}
    for key, value in sent.items():
        summation = 0 #Initializes the sum of the polarity rating for each line
        total = 0 #Initializes a counter for the total number of lines for a given person
        avg[key] = []
        for x in value:
            summation += x[1] #Adds the subjectivity data to the value. The sentiment function returns a list with polarity in the 1th position
            total += 1 #Increments the total number by 1 to represent the total number of spoken lines
        avg[key].append(summation/total) #Divides the sum by the total to provide an average subjectivity for each person
    return avg

def pattern_results(data): #Takes a CSV file as input (assumes names are in the first column and speech in the second) and prints the names of the participants along with the average calculations
    d = sort_data(data)
    avg_mod = average_modality(d)
    avg_pol = average_polarity(d)
    avg_sub = average_subjectivity(d)
    for key, value in d.items():
        if key != "male participant" and key != "female participant" and key != "non-team member" and key != '': #Ignores a number of common names that pop up in transscripts and are to be ignored
            print key + ":"
            print "Average Modality: " + str(avg_mod[key]) + ", Average Polarity: " + str(avg_pol[key]) + ", Average Subjectivity" + str(avg_sub[key])
            print "\n"
