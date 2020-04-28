from google.appengine.ext import ndb

class Images(ndb.Model):
    blobs = ndb.BlobKeyProperty()
