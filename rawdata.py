import tweepy
from alpha_vantage.timeseries import TimeSeries
import json



ALPHA_API_KEY = ''
CONSUMER_KEY = ''
CONSUMER_SECRET_KEY = ''
ACCESS_TOKEN = ''
ACCESS_SECRET_TOKEN = ''


if __name__ == '__main__':
    data = json.loads(open('API_KEYS.json', 'r').read())

    ALPHA_API_KEY = data['ALPHA_API_KEY']
    CONSUMER_KEY = data['CONSUMER_KEY']
    CONSUMER_SECRET_KEY = data['CONSUMER_SECRET_KEY']
    ACCESS_TOKEN = data['ACCESS_TOKEN']
    ACCESS_SECRET_TOKEN = data['ACCESS_SECRET_TOKEN']

    ts = TimeSeries(key=ALPHA_API_KEY)
    stock_data, meta_data = ts.get_intraday('TSLA')
    print (stock_data)


    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY);
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN);
    api = tweepy.API(auth);


    public_tweets = api.search('Tesla');

    for tweet in public_tweets:
        print (tweet.text)
