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
        id = self.request.get('id')
        user = users.get_current_user()
        
        myuser_key = ndb.Key('MyUser',id)
        myuser = myuser_key.get()

        post_details = []

        current_user = myuser.postkey

        for i in current_user:
            new_i = Post.get_by_id(i.id())
            post_details.append(new_i)


        # self.response.write(post_details)
        count1 = len(myuser.followers)
        count2 = len(myuser.following)

        template_values = {
                           'user' : myuser.email_address,
                           'post_details': post_details,
                           'Post': Post,
                           'count1': count1,
                           'count2': count2
                            # 'post' : post
        }

        template = JINJA_ENVIRONMENT.get_template('profilepage.html')
        self.response.write(template.render(template_values))
