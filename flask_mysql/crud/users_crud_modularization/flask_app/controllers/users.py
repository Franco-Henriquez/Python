# users.py
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

@app.route("/users")
def user_list():
    # call the get all classmethod to get all friends
    users = User.get_all()
    # print('User:',users[0].first_name)
    return render_template("users.html", all_users = users)

@app.route("/users/<int:user_id_from_url>")
def get_user_by_id(user_id_from_url):
    #naming _py for learning purposes
    user_info_py = User.get_by_id(user_id_from_url)
    return render_template("user_info.html",user_info=user_info_py)

@app.route("/users/<int:user_id_from_url>/delete")
def delete_user_by_id(user_id_from_url):
    # simply delete the user
    User.delete_by_id(user_id_from_url)
    return redirect("/users")

##########################################################################################################
##########################################################################################################
# EDIT PAGE
#                                                BECAUSE WE ARE BOTH RETRIEVING INFO
#                                                AND THEN POSTIING (UPDATING) IT
#                                                THIS NEEDS TO BE MADE
@app.route("/users/<int:user_id_from_url>/edit", methods=['POST','GET'])
def edit_user_by_id(user_id_from_url):
    # User.edit_by_id(user_id_from_url)
    user_info_py = User.get_by_id(user_id_from_url)
    return render_template("edit_user.html",user_info=user_info_py)
##########################################################################################################
# EDIT USER INFORMATION
@app.route("/users/<int:user_id_from_url>/update", methods=['POST'])
def update_user_by_id(user_id_from_url):
    # print("This is the request form",request.form)

    some_user = User.update_by_id(request.form,user_id_from_url)
    print("Some user", some_user)

    # after we update and proceed with form and query, we then retrieve that user's new ingo
    return redirect(url_for('get_user_by_id', user_id_from_url=user_id_from_url))
##########################################################################################################
##########################################################################################################

@app.route("/users/new")
def new_user():
    return render_template("add_user.html")

@app.route("/users/create", methods=['POST'])
def create_user():
    user_id = str(User.add_user(request.form))
    # at the same time that the user is created
    # load the /users/user_id url by going directly to the function
    # using url_for
    #
    #                         function name , parameter taken by function
    return redirect(url_for('get_user_by_id', user_id_from_url=user_id))
