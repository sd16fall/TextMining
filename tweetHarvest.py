# Sentiment Divergence Toolbox
# Anderson Ang Wei Jian, Mini Project 1
# Returns statistics on the variance of opinions with regards to a topic;
# This program requires (2) geolocations, restricted to capitals, and (1) topic of interest"
# Local and global polarity of content, opinionation, and modality levels are reflected

from pattern.web import Twitter , hashtags
from pattern.web.locale import geocode
from pattern.en import sentiment # sentiment library, to acquire polarity and subjectivity (is it positive/negative) and if its objective/subjective (tells how much of an opinion it is)
from pattern.en import modality # acquire modality (degree of certainty between fact or opinion)
from pattern.web import cache
from pattern.db import Datasheet, pprint, pd, SUM, AVG, STDEV, INTEGER, STRING
import re # the regex library for processing sentences
import datetime # library for system datetime
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
import time #for sleep function
# brand new - patch 1.0b - matplot display
import numpy as np
import matplotlib.pyplot as plt

# Opens a CSV(comma-separated value) file for identifying and storing unique tweets
try:
    table = Datasheet.load(pd("analysis.csv"),headers=False)
    index = set(table.columns[0])
# exceptions here
except:
    table = Datasheet(fields=[
    ("id", INTEGER),
    ("content", STRING),
    ("location",STRING),
    ("polarity",STRING),
    ("subjectivity",STRING),
    ("modality",STRING)])
    index = set()

# OMISSION WAS MADE HERE - private key accidentally uploaded, need to purge! OMG
# Declare Twitter object, to search for precise stream-based information
twitter = Twitter(license=None, throttle = 0.5, language='en')

# Function only sends live requests - by defining cached=False
# Note: Geocode identifies world capital cities, not country, for a more precise feedback
# Range controls the total run count of the program - Streams = range * count, producing more unique threading
def enrolTwitter(thread,location):
    # This function searches for the thread based on the specified location, and cleans the results
    # It also enrols the "cleaned" data into a CSV based file for analysis
    # setting marker (RT) for removal (improves sentient analysis results)
    remove_list =['RT']
    i = None # initalizing placeholder value to store Tweet IDs (ensure uniqueness)
    for j in range(2):
        # Count controls the number of streams returned at one time
        # RTs count as unique tweets, as long as the handler ID is unique
        print "Iteration Number", (j+1) #for humans to understand lulz
        print
        for tweet in twitter.search(thread, geo=geocode(location)[:2],start=i,count=5, cached=False):
            # adds tweet if its ID doesn't exist previously
            if len(table) == 0 or tweet.id not in index:
                # a series of sentence level filters designed for Twitter handles
                # decomposes the tweet into words, and weeds for items in the remove_list
                dcomp_tweet = (tweet.text).split()
                # removes RTs from the tweet
                recombined_tweet = ' '.join([k for k in dcomp_tweet if k not in remove_list])
                #removes hashtag related content
                stringwithouthash = re.sub(r'#\w+ ?', '', recombined_tweet)
                #removes http/s related content
                stringwithouthttp = re.sub(r'http\S+', '', stringwithouthash)
                #removes @ related content
                finalstring = re.sub(r'@\w+ ?','',stringwithouthttp)
                print finalstring
                # calls a function to analyze the string's sentiment value
                polarityVal, subjVal = checkSentiment(finalstring)
                # calls a simple function to analyze the string's certainty
                modalVal = checkModality(finalstring)
                table.append([tweet.id, finalstring,location,polarityVal,subjVal,modalVal,thread])
                index.add(tweet.id)
            # Continues mining for older tweets (varied by j value) in the second iteration
            i = tweet.id

    # Commit saves to the parent directory of the Python file
    print
    print
    print
    print "Harvest complete - saving to:", os.getcwd()
    table.save(pd("analysis.csv"), headers=False)
    print

    print "Total unique entries in table:", len(table)
    print


def verifyGeocode(location):
    if (geocode(location)[:2]) is not None:
        return True
    else:
        return False

def checkModality(sentence):
    return modality(sentence)

def checkSentiment(sentence):
    polarity, subjective = sentiment(sentence)
    return polarity, subjective

# demonstrates file access at this point
def localSentiment(location,topic):
    # recycleable variables - must be reinitialized every time function is called
    polarVal = 0.0
    subVal = 0.0
    modeVal = 0.0
    x = 0.0
    y = 0.0
    # opening location-based values in sentiment and modality for averaging
    for x in range(len(table)):
        if ((table[x,2]) == location) and (table[x,6] == topic):
            y+=1 # for averaging
            polarVal += float(table[x,3])
            subVal += float(table[x,4])
            modeVal += float(table[x,5])
    # average values
    print "x value is:", (x+1)
    print "y val is:", y
    avgPol = polarVal/y
    avgSub = subVal/y
    avgMode = modeVal/y
    return avgPol, avgSub, avgMode

def globalSentiment(topic):
    # takes a global average for comparison
    # recycleable variables - must be reinitialized every time function is called
    globalPolar = 0.0
    globalSub = 0.0
    globalMode = 0.0
    x = 0.0
    y = 0.0
    # opening location-based values in sentiment and modality for averaging
    for x in range(len(table)):
        if ((table[x,6] == topic)):
            y+=1 # for averaging
            globalPolar += float(table[x,3])
            globalSub += float(table[x,4])
            globalMode += float(table[x,5])
    # average values
    print "x value is:", (x+1)
    print "y val is:", y
    avgPol2 = globalPolar/y
    avgSub2 = globalSub/y
    avgMode2 = globalMode/y
    return avgPol2, avgSub2, avgMode2

# Human intepreter for the numerical data acquired
def forecast(topic,location1,location2,avgPol1,avgSub1,avgMode1,avgPol2,avgSub2,avgMode2):
    print
    print "=============== WHAT THIS MEANS ================"
    # Explains consequences of polarity
    if(avgPol1 > avgPol2):
        print location1, " views ", topic, " more positively than ", location2
    elif(avgPol2 > avgPol1):
        print location2, " views ", topic, " more positively than ", location1
    else:
        print "Both locales have the same level of opinion towards ", topic

    # Explains consequences of subjectivity
    if(avgSub1 > avgSub2):
        print location1, "is more opinioniated about", topic
    elif(avgSub2 > avgSub1):
        print location2, "is more opinioniated about", topic
    else:
        "Both locales are equally opinioniated about",topic

    # Explains consequences of modality
    if(avgMode1 > avgMode2):
        print location1, "'s stream contains more factual certainty about", topic
    elif(avgMode2 > avgMode1):
        print location2, "'s stream contains more factual certainty about", topic
    else:
        "Both locales are equal in factual certainty about",topic

    #finds the absolute difference between the polarities
    divergence = abs(avgPol1 - avgPol2)
    print
    print "Index divergence between the polarities: ", divergence

def userInterface():
    # text formatting block, purely for aesthetics, now funtionalized
    print "Here are a list of cities to choose from (for sample purposes)"
    print " 1. Singapore \n 2. Brussels \n 3. London \n 4. Paris \n 5. Beijing \n 6. Pretoria \n 7. Tokyo\n 8. Moscow\n"
    location = raw_input("Please enter a city name: (e.g. Singapore):")
    # checks if the geocode specified is valid
    while(verifyGeocode(location) is not True):
        print "Please try again!"
        location = raw_input("Please enter a city name: (e.g. Singapore):")
    print "You cleared the location test!"
    return location

def plotting(topic,location1,location2,avgPol1,avgSub1,avgMode1,avgPol2,avgSub2,avgMode2,globalPolar,globalSub,globalMode):
    # number of charts
    n_groups = 3

    loc1 = (avgPol1,avgSub1,avgMode1)
    std_1 = (1,2,3)

    loc2 = (avgPol2,avgSub2,avgMode2)
    std_2 = (1,2,3)

    loc3 = (globalPolar,globalSub,globalMode)
    std_3 = (1,2,3)

    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    # thickness of bar plot
    bar_width = 0.3

    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    rects1 = plt.bar(index, loc1, bar_width,
                    alpha=opacity,
                    color='b',
                    yerr=std_1,
                    error_kw=error_config,
                    label=location1)

    rects2 = plt.bar(index + bar_width, loc2, bar_width,
                    alpha=opacity,
                    color='r',
                    yerr=std_2,
                    error_kw=error_config,
                    label=location2)

    rects3 = plt.bar(index + (2*bar_width), loc3, bar_width,
                    alpha=opacity,
                    color='y',
                    yerr=std_3,
                    error_kw=error_config,
                    label='Average')


    plt.xlabel('Geolocation')
    plt.ylabel('Value')
    plt.title('Sentient analysis by geocodes')
    plt.xticks(index + bar_width, ('Polarity', 'Subjectivity', 'Modality'))
    plt.legend()

    plt.tight_layout()
    plt.show()

# Main program block
if __name__ == "__main__":
    print "=========== SENTIMENT ANALYSIS TOOL v1.0b =========="
    print
    print "Returns statistics on the variance of opinions with regards to a topic;"
    print "This program requires (2) geolocations, restricted to capitals, and (1) topic of interest"
    print
    # Phase I : Provides user guidance and takes first geolocation
    location1 = userInterface()
    # Phase II: Enrols topic and 2nd geocode
    topic = raw_input("Enter a phrase, word, question you would like to analyze:")
    enrolTwitter(topic,location1)
    print "Individual sentiment and modality committed."
    print
    print "Please prepare to enrol the second city:"
    print
    location2 = userInterface()
    enrolTwitter(topic,location2)
    print "Individual sentiment and modality committed."
    print
    print
    print "Calculating local and global sentiments and certainty.."
    print
    avgPol1, avgSub1, avgMode1 = localSentiment(location1,topic)
    print
    print location1, "statistics-\n Polarity:", avgPol1,"\n Subjectivity: ", avgSub1,"\n Modality:", avgMode1
    print
    avgPol2, avgSub2, avgMode2 = localSentiment(location2,topic)
    print
    print location2, "statistics-\n Polarity:", avgPol2,"\n Subjectivity: ", avgSub2,"\n Modality:", avgMode2
    print
    globalPol, globalSub, globalMode = globalSentiment(topic)
    print
    print "Global statistics -\n Polarity:", globalPol,"\n Subjectivity: ", globalSub,"\n Modality:", globalMode
    print
    time.sleep(1)
    # explanatory function to communicate the idea behind the statistics acquired
    forecast(topic,location1,location2,avgPol1,avgSub1,avgMode1,avgPol2,avgSub2,avgMode2)
    # PLUS : explanatory graph to communicate the scale of opinion
    print
    print "Creating plots and subplots.."
    print
    time.sleep(2)
    plotting(topic,location1,location2,avgPol1,avgSub1,avgMode1,avgPol2,avgSub2,avgMode2,globalPol,globalSub,globalMode)
    cache.clear() # empties the local search bin before terminating
