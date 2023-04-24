from flask import render_template, redirect, request, session
from flask_app.models import user #import file that has the user model
from flask_app import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 

# VISIBLE ROUTES
@app.route("/")
def login_reg_page():
    return render_template("home_page.html")

@app.route("/dashboard")
def dashboard_page():
    #if nobody is logged in, send client back to root
    if "user_id" not in session:
        return redirect("/")
    else:
        data = {
            "id": session["user_id"]
        }
        logged_in_user = user.User.get_user_by_id(data)
        return render_template("dashboard.html", this_user=logged_in_user)


# HIDDEN ROUTES
@app.route("/register", methods=['POST'])
def register_user_in_db():
    print("##################################\n\n")
    print(request.form)
    print("\n\n##################################")
    # validate the form here ...
    # create the hash
    #validate the form data before passing it to the db
    # if validate is NOT good then we pass flash messages to html
    if not user.User.validate_registration(request.form):
        return redirect("/")
    else:
        hashed_password = bcrypt.generate_password_hash(request.form['password'])
    # if validation is good, then add the user to the db
    # and then send the end user to the next route, the dashboard or other
        user_data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': hashed_password #always hash the password before sending to the model for db processing
        }
        session["user_id"] = user.User.add_user(user_data) # and now send user data to model to save new user to db

        return redirect("/dashboard")

@app.route("/login", methods=['POST'])
def login_user():
    # user_email = user.User.get_user_by_email(request.form['email'])
    # hashed_password = bcrypt.generate_password_hash(request.form['password'])
    # validate that someone exists with that email
    # and that the password is correct
    if not user.User.validate_login(request.form):
        return redirect("/")
    else: 
        user_email = {
            "email": request.form['email']
        }
        found_user = user.User.get_user_by_email(user_email)
        session['user_id'] = found_user.id
        return redirect("/dashboard")

@app.route("/logout")
def logout_user():
    session.clear()
    return redirect("/")