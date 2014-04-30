import tweepy2
import threading
import time
import re
import sys

consumer_key = "MYqFUyn5NbEF1crszsg"
consumer_secret = "ap1cOd6EFbsBRiGthTXrM0M6fN2RCPV0lYFoX1Ys"

access_token = "39950129-0tpjcB6dVKSalWLuBhE4uMsVryR5MBAntJWsudVuG"
access_token_secret = "FLn2dTqPRtDC1sF4tMRzXpoWXby0Na97OW3WA2hGEnME7"

auth = tweepy2.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy2.API(auth_handler=auth, proxy_url='172.31.16.10:8080')
user = api.me()
scr_name=sys.argv[1]
print scr_name
tweet_list = api.user_timeline(scr_name, count=200)

tweets = [tweet.text.encode('ascii', 'ignore') for tweet in tweet_list]
for t in tweets:
    print t
