import tweepy
from alpha_vantage.timeseries import TimeSeries
import json
import re
import vaderSentiment



ALPHA_API_KEY = ''
CONSUMER_KEY = ''
CONSUMER_SECRET_KEY = ''
ACCESS_TOKEN = ''
ACCESS_SECRET_TOKEN = ''

STOCK_NAME = 'TSLA'

analyzer = vaderSentiment.SentimentIntensityAnalyzer()

def generate_stocks_csv(ts):
    stock_data, meta_data = ts.get_daily(STOCK_NAME, outputsize='full')
    #stock_data.drop('2. high', 1)
    del stock_data['2. high']
    del stock_data['1. open']
    del stock_data['3. low']
    stock_data.to_csv(STOCK_NAME + '.csv', sep=',')

def cleanse_tweet(tweet):
    # process the tweets

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','username',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet

class TwitterStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        clean_status = cleanse_tweet(status.text)
        vs = analyzer.polarity_scores(clean_status)
        print(clean_status)
        print(vs)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

if __name__ == '__main__':
    data = json.loads(open('API_KEYS.json', 'r').read())

    ALPHA_API_KEY = data['ALPHA_API_KEY']
    CONSUMER_KEY = data['CONSUMER_KEY']
    CONSUMER_SECRET_KEY = data['CONSUMER_SECRET_KEY']
    ACCESS_TOKEN = data['ACCESS_TOKEN']
    ACCESS_SECRET_TOKEN = data['ACCESS_SECRET_TOKEN']

    ts = TimeSeries(key=ALPHA_API_KEY, output_format='pandas')
    generate_stocks_csv(ts)

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY);
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN);
    api = tweepy.API(auth);

    stream_listener = TwitterStreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    stream.filter(track=['Tesla', 'tesla', 'TSLA'])


    public_tweets = api.search('Tesla');

    for tweet in public_tweets:
        clean_tweet = cleanse_tweet(tweet.text)
        print(clean_tweet)
