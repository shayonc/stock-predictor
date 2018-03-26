import twitter
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import tweepy
from alpha_vantage.timeseries import TimeSeries



ALPHA_API_KEY = ''
CONSUMER_KEY = ''
CONSUMER_SECRET_KEY = ''
ACCESS_TOKEN = ''
ACCESS_SECRET_TOKEN = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY);
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN);

if __name__ == '__main__':
    #ts = TimeSeries(key=ALPHA_API_KEY)
    #data, meta_data = ts.get_intraday('TSLA')
    api = tweepy.API(auth);

    public_tweets = api.search('Tesla');

    for tweet in public_tweets:
        print tweet.text
        analysis = TextBlob(tweet.text, analyzer=NaiveBayesAnalyzer())
        print analysis.sentiment
