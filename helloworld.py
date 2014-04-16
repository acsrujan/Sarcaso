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
        self.response.write(str(user.id))
        self.response.write('\n')
	sutte_timeline = api.home_timeline()
        self.response.write('recieved home_timeline\n') 
        self.response.write(str(len(sutte_timeline))) 
        #self.response.write(str(dir(sutte_timeline[0])))
        #self.response.write(str(sutte_timeline))
	self.response.write('\n\n')

	for t in sutte_timeline:
	    print str(t)	 
        
        #text = "" 
        #for tweet in sutte_timeline:
        #    text = text + "\n" + tweet.text
        
application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
