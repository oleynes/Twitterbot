#recent message bot
import tweepy, time, sys
#Username of target
user = str(sys.argv[1])
#number of recent tweets
TWEET_EXTRACT = 5
#authorization stuff
CONSUMER_KEY = '8bCMIXRXaRjjK5orxLkqgp1K5'
CONSUMER_SECRET = 'HfVImYT6mYrSwtNoWyLDf9j82BbXtRY77J9qSAnUEAedDt3YPT'

ACCESS_KEY = '1035768467834716161-f8Go3f0o1ZAmTTUjfdvzwSw5DPGBeK'
ACCESS_SECRET = 'SQ7slJyksfzJXUNGhxZ1p4Qo0eDP5McritfdqNmfvDRDp'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
#get and print tweets from target
def get_tweets(username):
    tweets = api.user_timeline(screen_name=username)
    
    tweets_found = [tweet.text for tweet in tweets]
    for j in tweets_found:
        print j
        print ""
#exec   
if __name__ == '__main__':
    get_tweets(user)
