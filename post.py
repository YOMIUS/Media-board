from google.appengine.ext import ndb

class Post(ndb.Model):
    creator = ndb.KeyProperty()
    comments = ndb.StringProperty()
    imagekey = ndb.KeyProperty()
    imagekey_blob = ndb.BlobKeyProperty()
    caption = ndb.StringProperty()
    comments = ndb.StringProperty(repeated=True)
    date = ndb.DateTimeProperty()
