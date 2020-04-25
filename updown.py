import os
import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from myuser import MyUser
from post import Post
from images import BlobCollection
from google.appengine.ext.webapp import blobstore_handlers

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
    )

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        upload = self.get_uploads()[0]

        blobinfo = blobstore.BlobInfo(upload.key())
        filename = blobinfo.filename

        coll_key = ndb.Key('BlobCollection', 1)
        collection = coll_key.get()

        collection.filenames = filename
        collection.blobs = upload.key()
        collection.put()

        self.redirect('/')

class DownloadHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self):
        index = int(self.request.get('index'))

        coll_key = 
