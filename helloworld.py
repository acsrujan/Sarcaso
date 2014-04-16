"""A simple webapp2 server."""

import keys
import tweepy2
import webapp2

text = '<title>sarcaso</title><head>Website under maintenance<br></head>'

class MainPage(webapp2.RequestHandler):

    def get(self):

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(text)
	self.response.write('\n')
        
        auth = tweepy2.OAuthHandler(keys.consumer_key, keys.consumer_secret)
        auth.set_access_token(keys.access_token, keys.access_token_secret)
        
        api = tweepy2.API(auth)
        user = api.me()
        '''
        self.response.write(str(user.id))
        self.response.write('\n')
        '''
        '''
        #counter.main()
        '''

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
