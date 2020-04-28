import webapp2
import jinja2
import os
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from images import Images
from updown import UploadHandler
from updown import Display

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)
class NewPost(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'


        template_values = {
                'upload_url' : blobstore.create_upload_url('/upload'),
                }
        template = JINJA_ENVIRONMENT.get_template('newpost.html')
        self.response.write(template.render(template_values))
