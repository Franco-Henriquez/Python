from flask import redirect,session,render_template,request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

# @app.route('/dojos/<int:dojo_id_from_url>')
# def show_dojo(dojo_id_from_url):
#     dojo = Dojo.get_by_id(dojo_id_from_url)
#     print(dojo)
#     ninja = Ninja.get_by_dojo_id(dojo_id_from_url)
#     print(ninja.first_name)
#     return render_template('dojo.html', dojo=dojo, ninjas_in_dojo=ninja)




@app.route('/ninja')
def ninja():

    #allows us to get a list data of all the dojos from the dojos sql table
    dojos = Dojo.show_all_dojos()

    return render_template('ninja.html', dojos=dojos)

@app.route('/ninja/create', methods=['POST'])
def add_ninja():

    Ninja.add_ninja(request.form)

    return redirect('/dojos')