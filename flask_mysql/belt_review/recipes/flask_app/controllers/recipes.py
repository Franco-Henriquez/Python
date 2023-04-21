from flask import Flask, render_template, session, redirect, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

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

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_add_recipe(request.form):
        return redirect('/recipes/new')
    user_id ={
        'id': session['user_id']
    }
    #user_data becomes an object method, we would access it using dot notation
    user_data = User.get_by_id(user_id)
    # print("current user id:",session['user_id'])
    # print("USERS INFO:",user_data.first_name)
    recipe_data ={ 
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "under": request.form['under'],
        "date_cooked": request.form['date_cooked'],
        "posted_by": user_data.first_name,
        "user_id": user_data.id
    }
    Recipe.add_recipe(recipe_data)
    return redirect('/recipes')

