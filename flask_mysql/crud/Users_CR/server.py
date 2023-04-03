from flask import Flask, render_template, redirect, request
# import the class from friend.py
from user import User
app = Flask(__name__)

@app.route("/users")
def user_list():
    # call the get all classmethod to get all friends
    users = User.get_all()
    # print('User:',users[0].first_name)
    return render_template("users.html", all_users = users)

@app.route("/users/new")
def new_user():
    return render_template("add_user.html")

@app.route("/users/create", methods=['POST'])
def create_user():
    User.add_user(request.form)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)

