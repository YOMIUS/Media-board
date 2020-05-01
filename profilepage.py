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
        mainuser_key = ndb.Key('MyUser', user.user_id())
        mainuser = mainuser_key.get()

        id = self.request.get('id')
        myuser_key = ndb.Key('MyUser', id)
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
                           'myuser' : myuser,
                           'userr' : myuser.email_address,
                           'post_details': post_details,
                           'user' : user,
                           'Post': Post,
                           'count1': count1,
                           'count2': count2,
                           'mainuser' : mainuser
                            # 'post' : post
        }

        template = JINJA_ENVIRONMENT.get_template('profilepage.html')
        self.response.write(template.render(template_values))

    def post(self):
        user = users.get_current_user()
        id = self.request.get('id')
        follow = self.request.get('follow')
        unfollow = self.request.get('unfollow')

        myuser_key = ndb.Key('MyUser', user.user_id())
        myuser = myuser_key.get()

        newuser_key = ndb.Key('MyUser', id)
        newuser = newuser_key.get()

        if follow == 'follow':
            myuser.following.append(newuser.email_address)
            newuser.followers.append(myuser.email_address)
            myuser.timeline.append(id)
            myuser.put()
            newuser.put()

            self.redirect('/profile?id=' + id)
            # self.response.write(id)
            # self.redirect('/')

        if unfollow == 'unfollow':
            myuser.following.remove(newuser.email_address)
            newuser.followers.remove(myuser.email_address)
            myuser.timeline.remove(id)
            myuser.put()
            newuser.put()

            self.redirect('/profile?id=' + id)
            # self.redirect('/')
