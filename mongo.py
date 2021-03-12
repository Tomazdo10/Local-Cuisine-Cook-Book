import os
import pymongo
if os.path.exists("env.py"):
    import env 


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myDB"    
COLLECTION = "cuisine"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectFailure as e:
        print ("Could not connect to MongoDB: %s") % e


conn = mongo_connect("MONGO_URI") 

coll = conn[DATABASE][COLLECTION]

new_doc = {"name": "recipe_name", "ingredients": "recipe_ingredients", 
           "preperation": "preperation_time", "amount": "ingredients_amount",  
           "time": "preperation_time"}

coll.insert(new_doc)

documents = coll.find()

for doc in documents:
    print(doc)
    