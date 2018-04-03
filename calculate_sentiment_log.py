import pandas
from math import sqrt, log
import re
import vaderSentiment
from datetime import datetime
import holidays

us_holidays = holidays.UnitedStates() 

analyzer = vaderSentiment.SentimentIntensityAnalyzer()

def cleanse_tweet(tweet):
    
    #Convert to lower case
    tweet = tweet.lower()

    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)

    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','username', tweet)

    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)

    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)

    #trim
    tweet = tweet.strip('\'"')

    tweet = tweet.replace("\"", "")

    return tweet

if __name__ == '__main__':
    
    fd = open('sentiment_values_log.csv','w')
    fd.write("")
    fd.close()

    columns = ['username', 'date', 'retweets', 'favourites', 'text']
    df = pandas.read_csv('appended_output.csv', names=columns, sep=';')
    df2 = pandas.read_csv('TSLA.csv', sep=',')
    current_time = ""
    batch_time = ""
    counter = 1
    cumulative_compound = 0
    cumulative_sd_compound = 0
    avg_sentiment = 0
    squared_average = 0
    std_dev = 0

    for index, row in df.iterrows():
        tweet = cleanse_tweet(row['username'].split(';')[4])
        current_time = row['username'].split(';')[1].split(' ')[0]

        datetime_object = datetime.strptime(current_time, '%Y-%m-%d')

        if datetime_object.weekday() >= 5 or current_time in us_holidays:
            continue

        if batch_time == "":
            batch_time = current_time

        vs = analyzer.polarity_scores(tweet)
        if not current_time == batch_time:
            avg_sentiment = cumulative_compound / counter
            squared_average = (cumulative_sd_compound / counter)
            std_dev = sqrt(abs(squared_average - (avg_sentiment ** 2)))
            #write avg_sentiment to csv
            with open('sentiment_values_log.csv', 'a') as file:
                file.write("{0},{1},{2}\n".format(current_time, avg_sentiment, std_dev))
            print ("{0},{1},{2}".format(current_time, avg_sentiment, std_dev))
            counter = 1
            cumulative_compound = 0
            cumulative_sd_compound = 0
            batch_time = ""
        elif vs['compound'] == 0:
            counter = counter #no-op
        else:
            sentiment = float(vs['compound'])
            if sentiment < 0:
                sentiment += 1
                cumulative_compound += log(sentiment)
                cumulative_sd_compound += log(sentiment) ** 2
            else:
                sentiment = (sentiment * -1) + 1
                cumulative_compound += (-1 * log(sentiment))
                cumulative_sd_compound += (-1 * log(sentiment) ) ** 2
            counter = counter + 1
    print ("done")
