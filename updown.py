import webapp2
import jinja2

from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from post import Post
from datetime import datetime
from myuser import MyUser
from images import Images

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        upload = self.get_uploads()[0]

        user = users.get_current_user()
        myuser_key = ndb.Key('MyUser', user.user_id())
        myuser = myuser_key.get()

        image = Images()
        image.blobs = upload.key()
        image.put()

        post = Post()
        post.creator = myuser_key
        post.caption = self.request.get('caption')
        post.imagekey = image.key
        post.imagekey_blob = upload.key()
        post.date = datetime.now()
        post.put()

        # post_user = MyUser.get_by_id(myuser_key.id())
        myuser.postkey.append(post.key)
        myuser.put()

        self.redirect('/')

class Display(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, photo_key):
        if not blobstore.get(photo_key):
            self.error(404)
        else:
            self.send_blob(photo_key)
