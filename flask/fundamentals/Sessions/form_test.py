from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes



#SESSION PRACTICE
@app.route('/create_user')
def user_form():
    return render_template("/form_test/form_test.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user():
    # return render_template('/form_test/show.html', name_on_template=session['username'], email_on_template=session['useremail']) # can just use the simple form below because we are storing vars in sessions
    return render_template('/form_test/show.html')

if __name__=="__main__":
    app.run(debug=True, host="localhost", port=8200 )          