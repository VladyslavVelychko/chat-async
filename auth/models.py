from bson.objectid import ObjectId
from settings import USER_COLLECTION


class User():

    def __init__(self, db, data, **kw):
        self.db = db
        self.collection = self.db[USER_COLLECTION]