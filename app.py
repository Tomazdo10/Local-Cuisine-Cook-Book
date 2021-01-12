import os 
from flask import Flask, render_template, url_for, flash, \
            request, session, redirect, jsonify
from flask_pymongo import PyMongo
from passlib.hash import pbkdf2_sha256
from functools import wraps
import uuid
from bson.objectid import ObjectId
from bson.json_util import dumps
from os import path
if os.path.exists("env.py"):
        import env

    #Flask App

app = Flask(__name__)

app.secret_key = os.environ.get('SECRET KEY')    


#Clases
class User:
    def start_sesion(self, user):
        del user['password'] 
        session['loged_in'] = True
        session['user'] = user

        return jsonfy(user), 200

        def signup(self):

    #User Object
         user = {
    '_id': uuid.uuid4().hex,
    'name': request.form.get('name').lower(),
    'email': request.form.get('email').lower(),
    'password': request.form.get('password')}

#Encrypt password

user['password'] = pbkdf2_sha256.hash(user['password'])
if users.find_one({'email': user['email'].lower()}):
     jsonify({'error': 'Email address already in use'}),400
if users.insert_one(user):
     self.start_session(user)

     jsonify({"error": "Signup_failed"}),400

def signout(self):
    session .clear()
    return redirect(url_for('home_page'))

def login(self):
    email = request.form.get('email').lower()
    user = users.find_one({'email': email})

    if user and pbkdf2_sha256.verify (
        request.form.get('password'),
        user['password']):     

     return self.start_session(user)     

    return jsonify({'error': 'Invalid login'}),401   


def insert_recipe(self):
      recipe = {
          'user_id': session['user']['_id'],
          'recipe_name': request.form.get('recipe_name').lower(),
          'img_url': request.form.get('img_url'),
          'ingredient_name': request.form.getlist('ingredient_name'),
          'ingredient_amount': request.form.getlist('ingredient_amount'),
          'unit': request.form.getlist('unit'),
          'description': request.form.getlist('description')
      }    

      recipes.insert_one(recipe)

      return jsonify({'success': 'Recipe has been add'}),200

      def update_recipe(self, recipe_id):
          recipe = {
              'user_id': session['user']['_id'],
          'recipe_name': request.form.get('recipe_name').lower(),
          'img_url': request.form.get('img_url'),
          'ingredient_name': request.form.getlist('ingredient_name'),
          'ingredient_amount': request.form.getlist('ingredient_amount'),
          'unit': request.form.getlist('unit'),
          'description': request.form.getlist('description')
          }

          recipes.update({'_id': ObjectId(recipe_id)},recipe)

          return jsonify({'success': 'Recipe has been updated'}),200

#Database
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
app.config['MONGO_DBNAME'] = os.getenv('MONGO_DBNAME')
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
users = mongo.db.user_login_system
recipes = mongo.db.recipes

#Decorators      
    
def prevent_misuse(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            if 'logged_in' in session:
                return f(*args, **kwargs)
            else:
                return redirect(url_for('home_paige')) 

                return wrap       

def prevent_misuse(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('home_paige')) 

            return wrap       

@app.route('/')
@app.route('/home')
@prevent_misuse
def home_page():
        return render_template('index.html')

@app.route('/recipes', methods=['GET', 'POST'])  
def recipes_page():
    value_searched = request.form.get("search_value")
    if value_searched:
        cursor = recipes.aggregate([
            {"$search":{"text":  {"path": "recipe_name",
                                  "query": value_searched},
                                  "highlight": {"path": "recipe_name"}}},
            {"$project": {
                "_id": 1,
                "img_url": 1,
                "recipe_name": 1,
                "ingredient_name": 1,
                "ingredient_amount": 1,
                "unit": 1,
                "description": 1,
                "score": {"$meta": "searchScore"}}}]) 

    return render_template('recipes.html', all_recipes=cursor)

    return render_template('recipes.html', all_recipes=recipes.find())       

@app.route('/recipes/search', methods=['GET', 'POST'])
def search_data():
    query_text = request.form.get('search_value')

    if not query_text:
      cursor = recipes.find()

      list_cursor = list(cursor)
      json_data = dumps(list_cursor)

      return json_data, 200

    cursor = recipes.aggregate([
            {"$search":{"text":  {"path": "recipe_name",
                                  "query": query_text},
                                  "highlight": {"path": "recipe_name"}}},
            {"$project": {
                "_id": 1,
                "img_url": 1,
                "recipe_name": 1,
                "ingredient_name": 1,
                "ingredient_amount": 1,
                "unit": 1,
                "description": 1,
                "score": {"$meta": "searchScore"}}}]) 

    list_cursor = list(cursor)

    if not list_cursor:
        cursor = recipes.find()

        list_cursor = list(cursor)
        json_data = dumps(list_cursor)

        return json_data, 400 

        json_data = dumps(list_cursor)

        return json_data, 200           


@app.route("/about")
def about():
        data = []
        with open("data/cuisine.json", "r") as json_data:
            data = json.load (json_data)
            return render_template("about.html", site_title="About", cuisine=data)

#Contact
@app.route('/contact/')
def contact_page():
        return  render_template('contact.html')

#Login
@app.route('/login/')
@prevent_misuse
def login_paige():
            return render_template('login.html')    

@app.route('/user/login', methods=['GET', 'POST'])
@prevent_misuse
def login():
    user = User()
    return user.login()

#Add Recipe
@app.route("/add_recipe/") 
@login_required 
def add_recipe():
            return render_template("add_recipe.html")

@app.route('/add_recipe/insert_recipe', methods=['GET', 'POST'])
def insert_recipe():
            user = User()
            return user.insert_recipe() 

#Edit Recipe
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

#Update Recipe
@app.route('/update_recipe/<recipe_id>', methods=['GET', 'POST'])
@login_required
def update_recipe(recipe_id):
    User().update_recipe('recipe_id')
    return redirect (url_for('profile_page'))

#Delete Recipe
@app.route('/delete_recipe/<recipe_id>')
@login_required
def delete_recipe(recipe_id):
    recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('profile_page'))

#View Recipe
@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    recipe = recipes.find_one({'_id': ObjectId(recipe_id)})
    ingredients = zip(recipe['ingredient_name'],
                      recipe['ingredient_amount'],
                      recipe['unit'])

    return render_template('recipe.html', recipe=recipe,
                            ingredients=ingredients)                      

#Profile
@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username):
        #session user's username from mongodb
        username = mongo.db.user.find_one({
    "username", session["user"]})["username"]
if session["user"]:
     render_template("profile.html", username=username)
     redirect(url_for("login"))

#Logout
@app.route('/log_out')
def log_out():
       flash("You have been logged out")
       session.pop("user")
       return redirect(url_for('log_in'))  

#Register
@app.route('/register', methods=['GET', 'POST'])
def register():
       if request.method == "POST":

        existing_user = mongo.db.find_one(
    {"username": request.form.get("username").lower()})   

if existing_user():
     flash("Username already exists")
redirect(url_for("register"))
    
new_user = {
        "username": request.form.get("username").lower(),
        "password": generate_password_hash(request.form.get("password"))
    }

mongo.db.users.insert_one(new_user)

# Add user to session cookie
session["user"] = request.form.get("username").lower(),
flash("Registration Succsesful! You can now share your recipes!")
redirect(url_for("index", username=session["user"]))

render_template("register.html")
@app.errorhandler(404)
def error_404(error):
        return render_template('errors/404.html', error=True,
                                title='Paige not found'), 404

if __name__ == "__main__":
        app.run(
                host=os.environ.get("IP", "0.0.0.0"),
                port=int(os.environ.get("PORT", "5000")),
                debug=True)
