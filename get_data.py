import tweepy2
import threading
import time
import re
import sys

#consumer_key = 'zrDvgegV0K1lBLIxukR0A'
#consumer_secret = 'dM2BpTPoEvFBZ9oVVNSGUi5j1T6JQcCcE4At7TeNmw'
#access_token = '1270521626-CuXFTkLQ58yZbEj2memLErALqMcRbeVp4j8izxz'
#access_token_secret = 'Qh5Z620M5ttqs3QTE5LNFCRadNmA9XabfakNkbuKMJzdj'

consumer_key = "MYqFUyn5NbEF1crszsg"
consumer_secret = "ap1cOd6EFbsBRiGthTXrM0M6fN2RCPV0lYFoX1Ys"

access_token = "39950129-0tpjcB6dVKSalWLuBhE4uMsVryR5MBAntJWsudVuG"
access_token_secret = "FLn0dTqPRtDC1sF4tMRzXpoWXby0Na97OW3WA2hGEnME7"

auth = tweepy2.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy2.API(auth_handler=auth, proxy_url='172.31.16.10:8080')
scr_name=sys.argv[1]
print scr_name
user = api.me()

tweet_list = api.user_timeline(scr_name, count=200)
f = open(r'user_tweet_history', 'w')
for tweet in tweet_list:
    f.write(re.sub('\n+', ' ', tweet.text.encode('ascii','ignore'))+"\n")
