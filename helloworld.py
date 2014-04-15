"""A simple webapp2 server."""
import webapp2
import keys
#import tweepy

class MainPage(webapp2.RequestHandler):

    def get(self):

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('WEBSITE UNDER MAINTENANCE :P XD \n')
        
        #auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
        #auth.set_access_token(keys.access_token, keys.access_token_secret)
        
        self.response.write('Toekn set\n')
        #api = tweepy.API(auth)
        #user = api.me()

        #
        #self.response.write(str(user.id))
        #l=streamer.stream_func()
        #self.response.write(l)
        #counter.main()


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
