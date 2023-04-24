from flask import Flask, render_template, session, redirect, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


################
# VISIBLE ROUTES
################
@app.route('/recipes')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    recipes=Recipe.get_all()
    print("current user id:",session['user_id'])
    return render_template("recipes_dash.html",user=User.get_by_id(data),recipes=recipes)

@app.route('/recipes/new')
def create_pageview():
    user='blank'
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    if User.get_by_id(data) == False:
        return redirect('/logout')
    user_data = User.get_by_id(data)
    return render_template("new_recipe.html",user=user_data)

@app.route('/recipes/<int:recipe_id>')
def view_recipe(recipe_id):
    #user must be logged in and then pass the user's first_name to the page
    if 'user_id' not in session:
        return redirect('/logout')
    user_id ={
        'id': session['user_id']
    }
    if User.get_by_id(user_id) == False:
        return redirect('/logout')
    
    user_data = User.get_by_id(user_id)
    # since the user is logged in, let's now grab the recipe id
    # store in a dictionary
    recipe_id = {
        'id': recipe_id
    }
    # and fetch recipe data by id
    recipe_data = Recipe.get_recipe_by_id(recipe_id)


    return render_template("view_recipe.html",user_data=user_data,recipe=recipe_data)


################
# HIDDEN ROUTES
################
@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    print("##########################################\n\n")
    print("this is the request form:", request.form)
    print("\n\n##########################################")
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_add_recipe(request.form):
        return redirect('/recipes/new')
    user_id ={
        'id': session['user_id']
    }
    #user_data becomes an object method, we would access it using dot notation
    #use the reltionship with the foreign to pull this data.
    user_data = User.get_by_id(user_id)
    # print("current user id:",session['user_id'])
    # print("USERS INFO:",user_data.first_name)
    recipe_data ={ 
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "under_30": request.form['under_30'],
        "date_cooked": request.form['date_cooked'],
        # "posted_by": user_data.first_name,
        "user_id": user_data.id
    }
    Recipe.add_recipe(recipe_data)
    return redirect('/recipes')

