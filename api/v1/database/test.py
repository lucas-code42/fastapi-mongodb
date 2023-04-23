import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.test

print(db.my_collection)
# Collection(Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'test'),
# 'my_collection')
