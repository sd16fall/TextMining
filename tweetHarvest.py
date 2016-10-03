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

#license=('ZlvGyUbFwvh6huUZ02VCbG6JP','q9vhGij4NJOLWyKpQsFch5cSPnaATcY2AfrS6SSpaP901seIMk'
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
            #print tweet.text
            #print tweet.id
            #print
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

# Main program block
if __name__ == "__main__":
    # text formatting block, purely for aesthetics
    print "=========== SENTIMENT ANALYSIS TOOL v0.2b =========="
    print
    print "Returns statistics on the variance of opinions with regards to a topic;"
    print "This program requires (2) geolocations, restricted to capitals, and (1) topic of interest"
    print
    print "Here are a list of cities to choose from (for sample purposes)"
    print " 1. Singapore \n 2. Brussels \n 3. London \n 4. Paris \n 5. Beijing \n 6. Pretoria \n 7. Tokyo\n 8. Moscow\n"
    location1 = raw_input("Please enter a city name: (e.g. Singapore):")
    while(verifyGeocode(location1) is not True):
        print "Please try again!"
        location1 = raw_input("Please enter a city name: (e.g. Singapore):")
    print "You cleared the location test!"

    # Phase II: Enrol topic and geocode (not gonna functionalize for time's sake)
    topic = raw_input("Enter a phrase, word, question you would like to analyze:")
    enrolTwitter(topic,location1)
    print "Individual sentiment and modality committed."
    print
    print "Please prepare to enrol the second city:"
    print
    print "Here are a list of cities to choose from (for sample purposes)"
    print " 1. Singapore \n 2. Brussels \n 3. London \n 4. Paris \n 5. Beijing \n 6. Pretoria \n 7. Tokyo\n 8. Moscow\n"
    location2 = raw_input("Please enter a city name: (e.g. Paris):")
    while(verifyGeocode(location2) is not True):
        print "Please try again!"
        location2 = raw_input("Please enter a city name: (e.g. Singapore):")
    print "You cleared the location test!"
    enrolTwitter(topic,location2)
    print "Individual sentiment and modality committed."
    print
    print
    print "Calculating local and global sentiments and certainty.."
    print
    avgPol1, avgSub1, avgMode1 = localSentiment(location1,topic)
    print
    print location1, "statistics-\n Polarity:", avgPol1,"\n Subjectivity: ", avgSub1,"\n Modality:", avgMode1
    avgPol2, avgSub2, avgMode2 = localSentiment(location2,topic)
    print
    print location2, "statistics-\n Polarity:", avgPol2,"\n Subjectivity: ", avgSub2,"\n Modality:", avgMode2
    print
    time.sleep(1)
    # explanatory function to communicate the idea behind the statistics acquired
    forecast(topic,location1,location2,avgPol1,avgSub1,avgMode1,avgPol2,avgSub2,avgMode2)
    cache.clear() # empties the local search bin before terminating
