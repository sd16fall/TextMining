def tweet_list(hashtag, number):
    """
    Takes in a string and value find and returns a list of tweets the value
    long that contain the string
    """
    from pattern.web    import Twitter

    t = Twitter()
    i = None
    tweets = []
    for j in range(number):
        for tweet in t.search(hashtag, start=i, count=1):
            # print tweet.text
            # print
            tweets.append(tweet.text)
            i = tweet.id
    return tweets

def hastag_setiment(hashtag):
    """
    Takes in a hashtag and returns the average sentiment of a number of tweets
    with that hashtag
    """
    from pattern.en import *

    tweets = tweet_list(hashtag, 30)
    number_tweets = len(tweets)
    sentiment_sum = (0, 0)
    tweet_count = 0
    positivity_data = []
    subjectivity_data = []

    for j in range(number_tweets):
        tweet = tweets[j]
        senti = sentiment(tweet)
        # print sentiment(tweet)
        if senti[1] != 0:
            tweet_count += 1;
            sentiment_sum = (sentiment_sum[0]+ senti[0], sentiment_sum[1]+ senti[1])

    senti_avg = (sentiment_sum[0]/tweet_count, sentiment_sum[1]/tweet_count)
    # print sentiment_sum
    # print tweet_count
    return senti_avg

# hastag_setiment('#trump2016')

def compare_hashtags(hashtag_1, hashtag_2):
    """
    compares the sentiment and subjectivily of tweets that are associated with
    two different hashtags and out prints out a statement about the comparison
    """
    data_1 = hastag_setiment(hashtag_1)
    posi_1 = data_1[0]
    subject_1 = data_1[1]

    data_2 = hastag_setiment(hashtag_2)
    posi_2 = data_2[0]
    subject_2 = data_2[1]

    output = ''
    if posi_1 > posi_2:
        output = output + 'Tweets that use ' + str(hashtag_1) + \
            ' are currently more positive in sentiment then tweets that use ' \
            + str(hashtag_2)
    else:
        output = output + 'Tweets that use ' + str(hashtag_2) + \
            ' are currently more positive in sentiment then tweets that use ' \
            + str(hashtag_1)

    if subject_1 > subject_2:
        output = output + ' and tweets that use  ' + str(hashtag_1) + \
            ' are currently more subjective in sentiment then tweets that use ' \
            + str(hashtag_2) + '.'
    else:
        output = output + ' and tweets that use ' + str(hashtag_2) + \
            ' are currently more subjective in sentiment then tweets that use ' \
            + str(hashtag_1) + '.'

    print output

compare_hashtags('#trump2016', '#hillary2016')
