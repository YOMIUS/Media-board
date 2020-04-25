from google.appengine.ext import ndb

class MyUser(ndb.Model):
    email_address = ndb.StringProperty()
    post_key = ndb.KeyProperty(Post, repeated=True)
    followers = ndb.StringProperty(repeated=True)
    following = ndb.StringProperty(repeated=True)
