import os 
from flask import Flask, render_template, url_for,  request, flash, \
            request, session, redirect, jsonify
from flask_pymongo import PyMongo
import math
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from os import path
if os.path.exists("env.py"):
        import env

    #Flask App

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
app.config['MONGO_DBNAME'] = os.getenv('MONGO_DBNAME')
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
app.secret_key = os.environ.get('SECRET KEY')    

users = mongo.db.user_login_system
recipes = mongo.db.recipes

#Clases
class User:
    def start_sesion(self, user):
        del user['password'] 
        session['loged_in'] = True
        session['user'] = user
        
@app.route('/')
@app.route('/home')
def index():
        return render_template('index.html')

@app.route("/about")
def about():
        data = []
        with open("data/cuisine.json", "r") as json_data:
            data = json.load (json_data)
            return render_template("about.html", site_title="About", cuisine=data)

@app.route('/contact/')
def contact_page():
        return  render_template('contact.html')

@app.route('/login/')
def login_paige():
            return render_template('login.html')    

@app.route("/add_recipe/")  
@login_required()
def add_recipes():
            return render_template("add_recipe.html")

@app.route('/add_recipe/insert_recipe', methods=['GET', 'POST'])
def insert_recipe():
            user = User()
            return user.insert_recipe()   

@app.route("/edit_recipe/<recipe_id>")            
@login_required
def edit_recipe(recipe_id):
    recipe = recipes.find_one({'_id': ObjectId(recipe_id)})
    ingredients = zip(recipe['ingredient_name'],
                       recipe['ingredient_amount'],
                       recipe['unit'])
    return render_template('edit_recipe.html',
                           user_recipe=recipe,
                           user_ingredient=ingredients)                   

@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username):
        #session user's username from mongodb
        username = mongo.db.user.find_one({
    "username", session["user"]})["username"]
if session["user"]:
     render_template("profile.html", username=username)
     redirect(url_for("login"))

            #Decorators      
    
def prevent_misuse(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            if 'logged_in' in session:
                return f(*args, **kwargs)
            else:
                return redirect(url_for('home_paige')) 

                return wrap       

        # Search for recipe    

        @app.route("/search", methods=["GET", "POST"])
        def search():
            search = request.form["search"]
            print(search)

            recipe = mongo.db.recipe.find({"recipe_name":
                                        {"$regex": search, '$options': 'i'}})
            recipesName = mongo.db.recipe.find({"recipe_name":
                                            {"$regex": search, '$options': 'i'}}).count()

            print (recipesName)
            ingredients = mongo.db.recipe.find({"ingredients":
                                                {"$regex": search,
                                                '$options': 'i'}})

            ingredientsName = mongo.db.recipe.find({"ingredients":
                                                {"$regex": search,
                                                '$options': 'i'}}).count()

            print(ingredientsName)
            return render_template("search.html",
                                    recipe = recipe,
                                    ingredients = ingredients,
                                    recipesName = recipesName,
                                    ingredientsName = ingredientsName,
                                    )                       
        #Recipe Results
        @app.route("/view_search_result/<recipe_id>", methods=["GET"])
        def view_search_result(recipe_id):
            recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
            ingredients = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
            return render_template("full_recipe.html",
                                recipe=recipe, ingredients=ingredients)

@app.errorhandler(404)
def error_404(error):
        return render_template('errors/404.html', error=True,
                                title='Paige not found'), 404

if __name__ == "__main__":
        app.run(
                host=os.environ.get("IP", "0.0.0.0"),
                port=int(os.environ.get("PORT", "5000")),
                debug=True)
