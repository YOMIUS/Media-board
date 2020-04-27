from google.appengine.ext import ndb

class Images(ndb.Model):
    filename = ndb.StringProperty()
    blobs = ndb.BlobKeyProperty()
