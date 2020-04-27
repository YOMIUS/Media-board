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

class ProfilePage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'

        user = users.get_current_user()
        myuser_key = ndb.Key('MyUser', user.user_id())
        myuser = myuser_key.get()

        post_details = []

        current_user = MyUser.get_by_id(user.user_id()).postkey

        for i in current_user:
            post_details.append(i)


        self.response.write(post_details)


        template_values = {
                           'post_details': post_details,
                           'Post': Post
                            # 'post' : post
        }

        template = JINJA_ENVIRONMENT.get_template('profilepage.html')
        self.response.write(template.render(template_values))
