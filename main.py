import tweepy
import os

ck = os.environ["ck"]
cs = os.environ["cs"]

# Authenticate to Twitter
auth = tweepy.OAuthHandler(ck, cs)

ats = os.environ["ats"]
at = os.environ["at"]

auth.set_access_token(at, ats)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

api.update_status("")
