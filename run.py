import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
   import env

#Flask app

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET KEY')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
  data = []
  with open("data/cuisine.json", "r") as json_data:
    data = json.load (json_data)
    return render_template("about.html", site_title="About", cuisine=data)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print(request.form["email"])
        flash("Thanks{} we have recived your message!".format(
            request.form.get("name")))
    return render_template("contact.html", site_title="Contact")


@app.route("/find_recipes")  
def careers():
    return render_template("find_recipes.html", site_title="Find_Recipes")  


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
