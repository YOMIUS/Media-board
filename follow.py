import webapp2
import jinja2
import os
from google.appengine.api import users
from google.appengine.ext import ndb
from myuser import MyUser
from post import Post

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
    )

class Followers(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        user = users.get_current_user()
        id = self.request.get('id')

        myuser_key = ndb.Key('MyUser', id)
        myuser = myuser_key.get()

        template_values = {
                            'followers' : myuser.followers
        }

        template = JINJA_ENVIRONMENT.get_template('followers.html')
        self.response.write(template.render(template_values))

class Following(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        user = users.get_current_user()
        id = self.request.get('id')

        myuser_key = ndb.Key('MyUser', id)
        myuser = myuser_key.get()

        template_values = {
                            'following' : myuser.following
        }

        template = JINJA_ENVIRONMENT.get_template('following.html')
        self.response.write(template.render(template_values))
