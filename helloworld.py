"""A simple webapp2 server."""

#import counter
import webapp2



class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('WEBSITE UNDER MAINTENANCE :P XD')
        #counter.main()


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
