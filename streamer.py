from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="zrDvgegV0K1lBLIxukR0A"
consumer_secret="dM2BpTPoEvFBZ9oVVNSGUi5j1T6JQcCcE4At7TeNmw"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="1270521626-CuXFTkLQ58yZbEj2memLErALqMcRbeVp4j8izxz"
access_token_secret="Qh3Z620M5ttqs3QTE5LNFCRadNmA9XabfakNkbuKMJzdj"

tweets_read = []

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
This is a basic listener that just prints received tweets to stdout.

"""
    def on_data(self, data):
        #print data
        tweets_read.append(data)
        return True

    def on_error(self, status):
        #print status

def stream_func():
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['basketball'])
    stream.close()
    return str(tweets_read)
