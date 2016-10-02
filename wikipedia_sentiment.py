#scrapes wikipedia and performs sentiment analysis to figure out what wikipedia thinks about
#congress democrats and republicans

#imports pattern web
from pattern.web import *
#imports pattern natural language
from pattern.en import * 

def sentiment_finder(searchterm):
    """Finds sentiment of a given article on wikipedia.
        accepts string searchterm where searchterm is the title of a wikipedia article.
        Returns vector of (sentiment, objectivity)
        where sentiment is between -1.0 and 1.0 and objectivity is between 0 and 1"""
    try:
        article = Wikipedia().search(searchterm) #pull article from wikipedia 
        articletext = str.splitlines(article.plaintext().encode('utf-8')) # plain text as list of string lines of article
        founde = False #looking for articles that start with bulleted lists
        for i in range(len(articletext)): #loop thru and find the first line in the article 
                if articletext[i] == '* e':   #First line of article content marked by *e if article starts with bulleted lists
                        index = i
                        founde = True
                if founde == False:          #if we haven't found e yet, no bulleted list so we automatically pull 1st paragraph
                        index = 0
                
        return sentiment(articletext[index+2])     #return sentiment. +2 accounts for first empty lines
    except:
                                      #surprisingly some congressmen don't have wikipedia articles.
       return (0,0)                   #returns no wikipedia sentiment if error is thrown
                                      #(wikipedia article does not exist)
    
#populate list of current voting members of house and senate     
    
republicans = [] #empty list for republican names

democrats = [] #empty list for democrat names


senators = Wikipedia().search('Current members of the United States House of Representatives')  #pulls wikipedia article for senators
senatorsections = senators.sections[5] #pulls section of senators wikipedia article to read (voting members)
senatorlist = senatorsections.tables[0]#pulls list of current senators in table form

#iterates thru the table and classifies article names with Democrats and Republicans
for i in range(len(senatorlist.rows)):      
    namelist = senatorlist.rows[i][1] #pulls name in odd form [last, firstfirst last]
    namelength = (len(namelist)-((len(namelist)-3)/2)) #custom index based on how pattern returns the names
    name = namelist[namelength-1:len(namelist)] #grabs name in format [first last]
    if senatorlist.rows[i][3] == 'Republican':  #sorts republicans into republicans and democrats into democrats
        republicans.append(name.encode('utf-8'))#NOTE: encode to string
    if senatorlist.rows[i][3] == 'Democratic':
        democrats.append(name.encode('utf-8'))


republicanscores = [] #empty list for republican scores
democraticscores = [] #empty list for democrat scores

republicancount = 0.0 #counter of how many republican scores 
democratcount = 0.0 #counter of how many democratic scores

#iterate thru list of republicans and find sentiment

for i in republicans:
    print i
    republicancount += 1.0 #keep track of how many republican scores
    republicanscores.append(sentiment_finder(i))
    



#iterate thru list of democrats and find sentiment


for i in democrats:
    print i
    democratcount += 1.0 #keep track of how many democrat scores
    democraticscores.append(sentiment_finder(i))
  


republicanaverage = [0,0] #empty list for average republican scores
democrataverage = [0,0]#empty list for average democrat scores

#sum and average democrat and republican scores
for i in democraticscores:
    democrataverage[0] += i[0]
    democrataverage[1] += i[1]

for i in republicanscores:
    republicanaverage[0] += i[0]
    republicanaverage[1] += i[1]

republicanaverage[0] = republicanaverage[0]/republicancount
republicanaverage[1] = republicanaverage[1]/republicancount
democrataverage[0] = democrataverage[0]/democratcount
democrataverage[1] = democrataverage[1]/democratcount

#Print final scores
print "final scores"

print "Republicans"
print republicanaverage
print "Democrats"
print democrataverage
    
