import os
import webapp2
import jinja2
from datetime import datetime
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from myuser import MyUser
from post import Post
from images import Images
from updown import UploadHandler
# from updown import DownloadHandler
from updown import Display
from newpost import NewPost
from profilepage import ProfilePage

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
    )

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'

        url = ''
        url_string = ''
        Welcome = 'Welcome back '
        user = users.get_current_user()

        if user:
            url = users.create_logout_url(self.request.uri)
            url_string = 'logout'

            myuser_key = ndb.Key('MyUser', user.user_id())
            myuser = myuser_key.get()

            template_values = {
                                'j' : user.user_id(),
                               'url' : url,
                               'url_string' : url_string,
                               'user' : user,
                               'Welcome' : Welcome
            }
            template = JINJA_ENVIRONMENT.get_template('main.html')
            self.response.write(template.render(template_values))


            if myuser == None:
                Welcome = 'Welcome to the application'
                myuser = MyUser(id=user.user_id())
                myuser.email_address = user.email()
                myuser.put()
        else:
            url = users.create_login_url(self.request.uri)
            url_string = 'login'

            template_values = {
                           'url' : url,
                           'url_string' : url_string,
                           'user' : user,
                           'Welcome' : Welcome
            }
            template = JINJA_ENVIRONMENT.get_template('main.html')
            self.response.write(template.render(template_values))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        search = self.request.get('button')

        user = users.get_current_user()
        id = self.request.get('id')
        # myuser_key = ndb.Key('MyUser', id)
        # myuser = myuser_key.get()

        if search == 'search':
            userr = MyUser()
            userr.email_address = self.request.get('Search')

            # self.response.write(userr.email_address)

            if len(userr.email_address)!= 0:
                query = MyUser.query(MyUser.email_address == userr.email_address).fetch()

                template_values = {
                                   'query' : query,
                                   'user' : user,
                                   # 'j' : id
                }
                template = JINJA_ENVIRONMENT.get_template('main.html')
                self.response.write(template.render(template_values))
                return

        template_values = {
                            'j' : user.user_id(),
                           'url' : url,
                           'url_string' : url_string,
                           'user' : user,
                           'Welcome' : Welcome
        }
        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/new', NewPost),
    ('/upload', UploadHandler),
    # ('/download', DownloadHandler),
    ('/display/([^/]+)?', Display),
    ('/profile', ProfilePage)
], debug=True)
