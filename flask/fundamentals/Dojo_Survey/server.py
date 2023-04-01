from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

#SESSION CORE ASSIGNMENT - COUNTER
@app.route('/')
def index():
    # if 'visits' in session:
    #     session['visits'] += 1
    #     session['counter'] += 1
    # else:
    #     session['visits'] = 1
    #     session['counter'] = 1
    return render_template('index.html')

# @app.route('/destroy_session', methods=['POST'])
# def clear_counter():
#     if 'counter' in session:
#         session.clear()		# clears all keys
#         # session.pop('visits')		# clears a specific key
#     return redirect('/')

# @app.route('/add_x_counter', methods=['POST'])
# def add_x_counter():
#     if 'counter' in session:
#         #set session to      get number_of_visits from the html form, convert str to int and subtract 1 because the root visit, automatically adds a 1
#         session['counter'] += int(request.form['num_of_counter'])-1
#     return redirect('/')

# @app.route('/add_two_counter', methods=['POST'])
# def add_two_counter():
#     if 'counter' in session:
#         session['counter'] += 1
#     return redirect('/')

# @app.route('/add_one_counter', methods=['POST'])
# def add_one_counter():
#     return redirect('/')

@app.route('/process', methods=['POST'])
def process_form():
    session['full_name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['code_language']
    session['coding'] = request.form['coding']
    session['fav_color'] = request.form['color']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def process_results():
    session['full_name']
    session['location']
    session['language']
    session['coding']
    session['fav_color'] 
    session['comments']
    return render_template('result.html')


if __name__=="__main__":
    app.run(debug=True, host="localhost", port=8200 )          
