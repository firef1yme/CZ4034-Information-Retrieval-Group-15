import pandas as pd
import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

data = {}

for friend in tweepy.Cursor(api.friends, screen_name='verified').items():
    if(friend.lang == 'en'):
        tweets = []
        user = friend.screen_name
        try:
            for tweet in tweepy.Cursor(api.user_timeline, screen_name=user, include_rts=False).items():
                if(tweet.lang == 'en'):
                    tweets.append(tweet.text)

                    if(len(tweets) == 100):
                        print(len(data), user)
                        data[user] = tweets
                        break
        except (tweepy.TweepError, tweepy.error.TweepError) as e:
            print('Failed to query tweets from user ', user)

    if(len(data) % 100 == 0):
        df = pd.DataFrame.from_dict(data, orient='index')
        df.to_csv(r'dataset.csv', encoding='utf-8')
