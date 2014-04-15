"""A simple webapp2 server."""

<<<<<<< HEAD
import streamer
=======
#import counter
>>>>>>> c789b19b6c36b7781196ddd0bc279bf9cf87d844
import webapp2



class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('WEBSITE UNDER MAINTENANCE :P XD')
<<<<<<< HEAD
        l=streamer.stream_func()
        self.response.write(l)
=======
        #counter.main()
>>>>>>> c789b19b6c36b7781196ddd0bc279bf9cf87d844


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
