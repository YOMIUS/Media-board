from google.appengine.ext import ndb

class Comments(ndb.Model):
    creator = ndb.StringProperty()
    comment = ndb.StringProperty()
