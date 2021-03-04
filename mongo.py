import os
import pymongo
if os.path.exists("env.py"):
    import env 


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myDB"    
COLLECTION = "Cuisine"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectFailure as e:
        print ("Could not connect to MongoDB: %s") % e

conn = mongo_connect("MONGO_URI") 

coll = conn[DATABASE][COLLECTION]

documents = coll.find()

for doc in documents:
    print(doc)