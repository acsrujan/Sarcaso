"""A simple webapp2 server."""

import webapp2


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('WEBSITE UNDER MAINTENANCE :P XD')


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
