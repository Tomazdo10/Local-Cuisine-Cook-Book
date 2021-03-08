import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


def show_menu():
    print("")
    print("1. Add a recipe")
    print("2. Find a recipe by name")
    print("3. Edit a recipe")
    print("4. Delete a recipe")
    print("5. Exit")

    option = input("Enter option: ")
    return option



def get_record():
     print("")
    first = input("Enter Name of the recipe > ")
    second = input("Enter Recipe_ingredients > ")

    try:
        doc = coll.find_one({"first": first.lower(), "second": recipe_ingredients()})
    except:
        print("Error accessing the database")    

    if not doc:    
        print("")
        print("Error! no results found")

    return doc:    


def add_record():
    print("")
    first = input("Enter Name of the recipe > ")
    second = input("Enter Recipe_ingredients > ")
    recipe = input("Enter Amount of the ingredients > ")
    steps = input("Enter Method > ")
    url = input("Enter image > ")

    new_doc = {
        "first": first.lower(),
        "recipe": recipe_ingredients,
        "recipe": amount,
        "steps":  method,
        "url": image,   
    }

    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")

def main_loop():
    while True:
        option = show_menu()
        if option == "1":
          add_record()
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
main_loop()
