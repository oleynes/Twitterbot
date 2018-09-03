#Send immediate message
import tweepy, time, sys

message = str(sys.argv[1])

CONSUMER_KEY = '8bCMIXRXaRjjK5orxLkqgp1K5'
CONSUMER_SECRET = 'HfVImYT6mYrSwtNoWyLDf9j82BbXtRY77J9qSAnUEAedDt3YPT'

ACCESS_KEY = '1035768467834716161-f8Go3f0o1ZAmTTUjfdvzwSw5DPGBeK'
ACCESS_SECRET = 'SQ7slJyksfzJXUNGhxZ1p4Qo0eDP5McritfdqNmfvDRDp'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status(message)
