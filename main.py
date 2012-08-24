import urllib2
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        long = self.request.get('long')
        lat = self.request.get('lat')
        response = urllib2.urlopen("http://free.worldweatheronline.com/feed/weather.ashx?q="+long+","+lat+"&format=json&num_of_days=2&key=58f929cfa0080459120901")
        self.response.out.write(response.read())

application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()