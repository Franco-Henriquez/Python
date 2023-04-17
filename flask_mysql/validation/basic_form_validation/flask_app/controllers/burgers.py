from flask_app import app
from flask import render_template,redirect,request,session,flash,url_for
from flask_app.models.burger import Burger


@app.route('/')
def burger_form():
    return render_template('index.html')


@app.route('/create', methods=['POST'])
def create_burger():
    # if there are errors:
    # We call the staticmethod on Burger model to validate
    if not Burger.validate_burger(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # else no errors:
    # here we can take the form data (immutable dictionary) by pieces and rebuild it into a dictionary (eidtable)
    data = {
        "name":request.form['name'],
        "bun":request.form['bun'],
        "meat":request.form['meat'],
        "calories":request.form['calories'],
        # now this one we add manually since we don't have an option for restaurant ids yet
        "restaurant_id":'1'
    }
    # since we took the request.form apart, we will comment out passing it
    # Burger.save(request.form)
    # and instead we pass the rebuilt data as so:
    Burger.save(data)
    return redirect("/burgers")

@app.route('/burgers')
def burger_list():
    return render_template('results.html',burger_list=Burger.get_all())