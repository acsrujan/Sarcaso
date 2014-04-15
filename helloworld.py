"""A simple webapp2 server."""
import streaming
import auth
import oauth
import webapp2
import module

class MainPage(webapp2.RequestHandler):

    def get(self):

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('WEBSITE UNDER MAINTENANCE :P XD \n')
        
        self.response.write(module.constant)
        
        consumer_key="zrDvgegV0K1lBLIxukR0A"
        consumer_secret="dM2BpTPoEvFBZ9oVVNSGUi5j1T6JQcCcE4At7TeNmw"
        access_token="1270521626-CuXFTkLQ58yZbEj2memLErALqMcRbeVp4j8izxz"
        access_token_secret="Qh3Z620M5ttqs3QTE5LNFCRadNmA9XabfakNkbuKMJzdj"
        
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        
        api = tweepy.API(auth)
        user = api.me()
        
        self.response.write(str(user.id))
        #l=streamer.stream_func()
        #self.response.write(l)
        #counter.main()


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
