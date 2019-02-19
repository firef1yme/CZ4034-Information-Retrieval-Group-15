import pandas as pd
import tweepy

consumer_key = 'CAFQUfr5Tw3rYhTdEXl1x350M'
consumer_secret = '3DouNQo4oEaLStSSWORJB3EQrX5FIg9k7DTvpYJTLAKETeqnEk'
access_token = '1096400473060327426-pLF9C8lFvtwOvsJOyP1zSVxQiZ9xz1'
access_token_secret = 'oczm1RtGSSnU1uTwPBwfxXtewYwi3Duev16qZKn70i3eZ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

data = {}

for friend in tweepy.Cursor(api.friends, screen_name='verified').items():
    if(friend.lang == 'en'):
        tweets = []
        user = friend.screen_name
        try:
            for tweet in api.user_timeline(screen_name=user, include_rts=False):
                if(tweet.lang == 'en'):
                    tweets.append(tweet.text)

                    if(len(tweets) == 10):
                        print(len(data), user)
                        data[user] = tweets
                        break
        except tweepy.TweepError:
            print('Failed to query tweets from user ', user)

df = pd.DataFrame.from_dict(data, orient='index')
df.to_csv(r'dataset.csv', encoding='utf-8')
