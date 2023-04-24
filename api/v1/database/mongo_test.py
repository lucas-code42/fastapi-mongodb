import pymongo
from uuid import uuid4

client = pymongo.MongoClient("mongodb://root:root@:27017")
db = client.test
collection = db.users
collection.insert_one(
    {
        "id":str(uuid4()), 
        "name": "test1", 
        "password": "test1", 
        "email": "test1"
    }
)

print(collection) # Collection(Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'test'), 'my_collection')



