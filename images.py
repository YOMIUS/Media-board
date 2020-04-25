from google.appengine.ext import ndb

class BlobCollection(ndb.Model):
    filenames = ndb.StringProperty()
    blobs = ndb.BlobKeyProperty()
