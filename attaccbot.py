#Targeted Twitter Troll

#imports
import tweepy, time, sys, schedule
#required auth key stuff
CONSUMER_KEY = '8bCMIXRXaRjjK5orxLkqgp1K5'
CONSUMER_SECRET = 'HfVImYT6mYrSwtNoWyLDf9j82BbXtRY77J9qSAnUEAedDt3YPT'

ACCESS_KEY = '1035768467834716161-f8Go3f0o1ZAmTTUjfdvzwSw5DPGBeK'
ACCESS_SECRET = 'SQ7slJyksfzJXUNGhxZ1p4Qo0eDP5McritfdqNmfvDRDp'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
###############################################################################
#Globals:

#Time between tweets:
TWEET_FREQ = 86400  #24 hours
#Tweet at a specific time
SCHEDULE_TWEET = False
SCHEDULE_TIME = "12:00" #12:00 PM
#Target of tweets
TWEET_TARGET = "EricAfterSchool"
#Log Tweets from target:
TWEET_LOG = False
#Log file
TWEET_LOG_LOC = "log.txt"
###############################################################################

#On exec if specific tweet is desired immediately, enter tweet string
if len(sys.argv) > 0:
    tweet = str(sys.argv[1])
    print "[*] Tweeting %s ..." % tweet
    api.update_status(tweet)

