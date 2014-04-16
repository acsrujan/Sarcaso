"""A simple webapp2 server."""

import keys
import tweepy2
import webapp2

text = '<title>sarcaso</title><head>Website under maintenance<br></head>'
new_line = '<p><br></p>'

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

	self.response.write(str(sutte_timeline[0].text))
	i=0
	feed_length = len(sutte_timeline)
	
	self.response.write(str(sutte_timeline[i].text))
	while i<feed_length:
	    self.response.write(str(sutte_timeline[i].text))
	    self.response.write(new_line)
	    i+=1
	
	#for t in sutte_timeline:
	#    self.response.write(new_line)
	#    self.response.write(str(t.text))
	     
        #text = "" 
        #for tweet in sutte_timeline:
        #    text = text + "\n" + tweet.text
        
application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
