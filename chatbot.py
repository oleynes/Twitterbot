#First real twitter bot

import tweepy, time, sys
#number of tweets to extract
TWEET_EXTRACT = 200
#authorization
CONSUMER_KEY = '8bCMIXRXaRjjK5orxLkqgp1K5'
CONSUMER_SECRET = 'HfVImYT6mYrSwtNoWyLDf9j82BbXtRY77J9qSAnUEAedDt3YPT'

ACCESS_KEY = '1035768467834716161-f8Go3f0o1ZAmTTUjfdvzwSw5DPGBeK'
ACCESS_SECRET = 'SQ7slJyksfzJXUNGhxZ1p4Qo0eDP5McritfdqNmfvDRDp'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
#get tweets function
def get_tweets(username):
    tweets = api.user_timeline(screen_name=username)
    tmp=[]
    tweets_found = [tweet.text for tweet in tweets]
    for j in tweets_found:
        tmp.append(j)
    
    print(tmp)

#exec
if __name__ == '__main__':
    get_tweets("EricAfterSchool")

