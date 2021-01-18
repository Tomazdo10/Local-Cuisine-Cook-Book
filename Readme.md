# Milestone Project 3 - Local Cuisine Cook Book
-----------------------------------------------
Local Cuisine Cook Book is a built app from the knowledge and learning process which i've learned from 
all the modules and other projects i've done so far with Code Institute.

The Milestone project includes HTML,CSS,JavaScript,Python,MongoDB and Heroku.
Local Cuisine Cook Book is a fully responsive database-backed, Flask web application.
It is build and designed for the user's wants and needs, while ensuring that the site has a 
user friendly and interactive design expectation.

You can view the live website here:

Using the CRUD('Create, Read, Update, and Delete,') model of the website has been created to provide an online recipe cook Book
so the users can add their recipe, all they have to do is signup. Users are able to store,view,edit and delite their recipes
They can also create an account which will recognize them when they will login back to their account.
Users can also see the website and some added recipes but they would not be able to add,or delete if they didn't join the
the community one the website.

## Contents
----------------------------------------------------------------------
1. UX
  * User Stories
2. Wireframes
3. Scope 
4. Features 
  * Features to add in Future
5. design
6. Technologies Used
7. Tools Used
8. Testing
   * User story Testing
9. Deployment
  * Deploying to Heroku
  * Clone and run localy
10. Secret key & Variables
11. Design
12. Credits
13. Acknowledgements

## UX
---------------------------------------------------------------------------------

Wtih the Local Cuisine Cook Book we can learn from other comunities and other parts of the world,
how the food looks like and taste like so we can learn some new reciepies and dishehs made from all
over the world and try something new.

The website has already some recipes from the site owner to follow also it gives the example how 
the format looks like and enable users to have recipes ready available while the website is still new.
It also encourage othe users to create a free account and share their recipes of their own.

### User Stories
------------------------------------------------------------------------------------------------

### New External User Goals
 
 * As a new user i want to be able to view recipes.
 * As a new user i want to be able to register and post my own recipes and serch for existing ones.
 
 ### Frequent User Goals
 ------------------------------------------------------------------------------------------------
  * As a frequent user i want to be able to continue to share my recipes in an easy way.
  * As a user i want to be able to find new reecipes from others users and see who posted them.
  * As an user i want to share my recipes to social media pages.

  ### Returning External User Goals:
  -----------------------------------------------------------------------------------------------
   * As a returning user i want to be able to edit and update my posted recipes.
   * As a returning user i want to be able to delete my posted recipes.

   ### Site Owner User Goals

   * As the site owner and developer i want to push my current learning skills to another level and 
   make a site that's useful and beneficial for other users.

   ### Wireframes
   -----------------------------------------------------------------------------------------------
   Using the user stories , I put together the wireframes for the Local Cuisine Cook Book using Balsamiq.
   The Wireframes coverd desktop, tablet and mobile formats.

   ### Changes in Wireframes?????

   * 
   * 
   *  

   ### Scope
   ------------------------------------------------------------------------------------------------

*  The user can find a recipes to cook themselves.

* The user can register to the website.

* The user can submit their own recipes to the website.

* The user can delete and edit the recipe on the website.

* The user can search for the recipes and find some they would like to try themselfs to cook.

    ## Existing Website Features
    ---------------------------------------------------------------------------------------------
       NAVIGATION BAR: Allows users to navigate to the relevant section on the website, such as log in/log out
       they can add the recipes, find a recipe and user profile page where they can see their username, links to
       home paige and add paige.

    
       EDIT RECIPE BUTTON: User will be able to edit their own recipe when he/she is sign in by clickong on the      
       edit button, but they will not be able to edit recipes from other users.      

       LOGIN: User can Log In to their accounts simply by using username and password form. Once they are logged     
       in users with the help of MongoDB can add, edit or delete the recepies as well as search for recipes added by other users.      

       REGISTER: The register section will allow users to register to a website so they can add, edit or delite     
       recipes as well share them with others and search for recipes added from other users, first they will need     
       to fill up the form with a username and password which they can use it every time they will logged in.      

       THE ABILITY TO UPLOAD THE IMAGE: User will be able to upload the image with the recipe via Add recipe     
       and Edit Recipe form by including the URL to the image.      

       SEARCH BAR: Allows users to input the text that is used for search, display and query recipes to the users.     
       Search bar function is created using the JavaScript ajax method to send and recieve data.      

      EmailJS: The Website has available form where users can use it to send us the email.This was set with      
      using the EmailJS [https://www.emailjs.com/] service. The user will need to fill up three forms "Full Name",     
      "Email" and "Message" once everything is filled, the user can send us na email by clicking on a send buttonwhich uses      
      the EmailJS service to send us the email.


Features Left to Implement
----------------------------------------------

 * Ability for users to upload a profile image
 * Developing system that will allow users to create
   group folders to create and storage the recipes there together.
* Create a function to download or storage other people recipes.

## Technologies Used for Developing

* Bootstrap [https://getbootstrap.com/]
   * The project website is using Bootstrap to provide the responsive toolkit for building the base of the website.

* Flask [https://www.fullstackpython.com/flask.html]
   * The project website is using Flask framework to provide the tools for developer that Allows
     to build a website aplication faster.

* Font Awesome [https://fontawesome.com/]
   * The project is using font awesome to use the icons for the website.

*  GitHub [https://github.com/Github]     
   * The project is using GitHub for version control.

* Python [https://www.python.org/]       
   * The project is using Python for routing and CRUD function.

* Heroku [https://dashboard.heroku.com/apps]
   * The project is using Heroku to deploy finished project.

* EmaiJS [https://www.emailjs.com/]
   * The project is using EmailJS for sending emails from website.

* MongoDB-Atlas [https://www.mongodb.com/cloud/atlas/lp/try2?utm_source=bing&utm_campaign=bs_emea_united_kingdom_search_brand_atlas_desktop&utm_term=mongodb%20atlas&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=386028215&msclkid=47a6a9a906941a57c371c9af0c6a75d5]         
   * The project is using MongoDB-Atlas to store the data on this website

* JQuery [https://jquery.com/]
  * The project is using JQuery to simplify the DOM manipulation.

* Google Fonts [https://fonts.google.com/]   
  * The project uses the Google Fonts to changing the font-famaly.

## Scheme Design
-------------------------------------------------------------------------------------
* After the research for the elements of the website and the items needed to be stored 
  I've retrive it from database for two collections:

   * Users: for register and login they contain the Object ID, Username and Password.

   * Recipes: contains the element required for CRUD (create,read,update and delete).
    The values for the recipe collection are added into the database and pulled from the 
    database by users in the section AddRecipe,EditRecipe and ViewRecipe and also for delete
    the recipe from database.

#### Users: 
  * _id: to be able to find the user by assigning a uniq id.

  * username: where the username would like to be recognized as posting and editing the recipe to the site.

  * Password: The password for user to be able to login to the website.  

#### Recipes:
  * _id: Unique identifier for the recipe

  * Find_recipe: The search bar where user can find others users upload recipes

  *  recipe_name: The recipe name the user gives to the recipe.

  * image_url: a url to be suplied by user to add the image to their recipe.

  * ingredient_amount: where user can add amount and description of the recipe.

  * step_description: where user can describe the recipe step by step how to use it.       