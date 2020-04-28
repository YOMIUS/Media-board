from google.appengine.ext import ndb
from post import Post

class MyUser(ndb.Model):
    email_address = ndb.StringProperty()
    postkey = ndb.KeyProperty(repeated=True)
    followers = ndb.StringProperty(repeated=True)
    following = ndb.StringProperty(repeated=True)
