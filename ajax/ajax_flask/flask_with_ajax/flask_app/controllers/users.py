from flask_app.models.user import User
from flask_app import app
from flask import make_response, render_template, jsonify, request, redirect




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users')
def users():
    return jsonify(User.get_all_json())


@app.route('/create/user',methods=['POST'])
def create_user():
    print("This is the request form data:",request.form)
    user_data = {
        "user_name": request.form['name'],
        "email": 'somemadeupemail@email.com'
    }
    # write code to save it to our database . . .
    return jsonify(User.save(user_data))




