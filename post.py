from google.appengine.ext import ndb
from comments import Comments

class Post(ndb.Model):
    creator = ndb.KeyProperty()
    imagekey = ndb.KeyProperty()
    imagekey_blob = ndb.BlobKeyProperty()
    caption = ndb.StringProperty()
    comments = ndb.StructuredProperty(Comments, repeated=True)
    date = ndb.DateTimeProperty()
