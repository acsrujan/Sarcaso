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
	text = ''
        self.response.write(str(len(sutte_timeline))) 
        #for t in sutte_timeline:
        #    text = '\n'+ str(t.id) + '\t' +  str(t.screen_name) + '\t'  + str(t.text)
        
        #self.response.write(text) 

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
