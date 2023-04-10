from flask import redirect,session,render_template,request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def index():
    dojos = Dojo.show_all()
    return render_template('index.html', dojos=dojos)

@app.route('/dojos/create', methods=['POST'])
def create():
    dojo = Dojo.create_dojo(request.form)
    print(dojo)
    return redirect('/dojos')