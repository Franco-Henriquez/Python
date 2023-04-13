from flask import redirect,session,render_template,request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/dojos')
def index():
    dojos = Dojo.show_all_dojos()
    return render_template('index.html', dojos=dojos)

@app.route('/dojos/create', methods=['POST'])
def create():
    dojo = Dojo.create_dojo(request.form)
    print(dojo)
    return redirect('/dojos')


@app.route('/dojos/<int:dojo_id_from_url>')
def show_dojo(dojo_id_from_url):
    # this comes back as a single object list
    dojo = Dojo.get_by_id(dojo_id_from_url)
    print(dojo)
    # when this is called, it comes back as a list
    ninja = Ninja.get_by_dojo_id(dojo_id_from_url)
    # so in order to test this, we just access the very first index (0) 
    # and try to grab wtv first_name we get
    print(ninja[0].first_name)
    return render_template('dojo.html', dojo=dojo, ninjas_in_dojo=ninja)