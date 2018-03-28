import tweepy
from alpha_vantage.timeseries import TimeSeries
import json



ALPHA_API_KEY = ''
CONSUMER_KEY = ''
CONSUMER_SECRET_KEY = ''
ACCESS_TOKEN = ''
ACCESS_SECRET_TOKEN = ''

STOCK_NAME = 'TSLA'


if __name__ == '__main__':
    data = json.loads(open('API_KEYS.json', 'r').read())

    ALPHA_API_KEY = data['ALPHA_API_KEY']
    CONSUMER_KEY = data['CONSUMER_KEY']
    CONSUMER_SECRET_KEY = data['CONSUMER_SECRET_KEY']
    ACCESS_TOKEN = data['ACCESS_TOKEN']
    ACCESS_SECRET_TOKEN = data['ACCESS_SECRET_TOKEN']

    ts = TimeSeries(key=ALPHA_API_KEY, output_format='pandas')
    stock_data, meta_data = ts.get_daily(STOCK_NAME, outputsize='full')
    #stock_data.drop('2. high', 1)
    del stock_data['2. high']
    del stock_data['1. open']
    del stock_data['3. low']
    stock_data.to_csv(STOCK_NAME + '.csv', sep=',')
    print (meta_data)
    print (stock_data)


    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY);
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN);
    api = tweepy.API(auth);


    public_tweets = api.search('Tesla');

    for tweet in public_tweets:
        print (tweet.text)
