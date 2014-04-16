"""A simple webapp2 server."""

import keys
from tweepy2.streaming import StreamListener
from tweepy2 import OAuthHandler
from tweepy2 import Stream
import webapp2

text = '<title>sarcaso</title><head>Website under maintenance<br></head>'

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
This is a basic listener that just prints received tweets to stdout.

"""
    def on_data(self, data):
        self.response.write(str(data))
        return True

    def on_error(self, status):
        self.response.write(str(status))

class MainPage(webapp2.RequestHandler):

    def get(self):

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(text)
	    self.response.write('\n')
        
        l = StdOutListener()
        
        auth = OAuthHandler(keys.consumer_key, keys.consumer_secret)
        auth.set_access_token(keys.access_token, keys.access_token_secret)
        
        '''
        api = tweepy2.API(auth)
        user = api.me()
        
        self.response.write(str(user.id))
        self.response.write('\n')
        '''
        
        stream = Stream(auth, l)
        stream.filter(track=['election'])
        #counter.main()


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
