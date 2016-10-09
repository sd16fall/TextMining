from pattern.en import sentiment
from pattern.en import modality

def sort_data(data):
    fin = open(data)
    d = {}
    names = []
    speech = []
    for line in fin:
        line1 = line.replace(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,","",1)
        line2 = line1.replace("\x92", "'")
        line3 = line2.replace("\x85", "")
        text = line3.replace("\r\n", "")
        key = text[0:text.index(',')]
        if key.strip() in d:
            d[key.strip()].append(text[text.index(',')+1:len(text)])
        else:
            d[key.strip()] = [text[text.index(','):len(text)]]
    return d

def get_sentiment(data):
    d = sort_data(data)
    sent = {}

    for key, value in d.items():
        sent[key] = []
        for x in value:
            sent[key].append(sentiment(x))
    return sent

def get_modality(data):
    d = sort_data(data)
    mod = {}

    for key, value in d.items():
        mod[key] = []
        for x in value:
            mod[key].append(modality(x))
    return mod

def average_modality(data):
    mod = get_modality(data)
    avg = {}
    for key, value in mod.items():
        summation = 0
        total = 0
        avg[key] = []
        for x in value:
            summation += x
            total += 1
        avg[key].append(summation/total)
    return avg

def average_polarity(data):
    sent = get_sentiment(data)
    avg = {}
    for key, value in sent.items():
        summation = 0
        total = 0
        avg[key] = []
        for x in value:
            summation += x[0]
            total += 1
        avg[key].append(summation/total)
    return avg

def average_subjectivity(data):
    sent = get_sentiment(data)
    avg = {}
    for key, value in sent.items():
        summation = 0
        total = 0
        avg[key] = []
        for x in value:
            summation += x[1]
            total += 1
        avg[key].append(summation/total)
    return avg

def pattern_results(data):
    d = sort_data(data)
    avg_mod = average_modality(data)
    avg_pol = average_polarity(data)
    avg_sub = average_subjectivity(data)
    for key, value in d.items():
        if key != "Male Participant" and key != "Female Participant" and key != "Non-team member":
            print key + ":"
            print "Average Modality: " + str(avg_mod[key]) + ", Average Polarity: " + str(avg_pol[key]) + ", Average Subjectivity" + str(avg_sub[key])
            print "\n"
