from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     


#THIS IS A STATIC EXAMPLE OF name phrase and times
@app.route('/')
def index():
    return render_template("index.html", name="Piers" ,phrase="hello", times=5)	# notice the 2 new named arguments!

#THIS IS DYNAMIC BECAUSE WE USE URL TO PASS INFO
@app.route('/<string:name>/<string:phrase>/<int:times>')
def index(name,phrase,times):
    return render_template("index.html", name=name ,phrase=phrase, times=times)	# notice the 2 new named arguments!




@app.route('/dashboard')                           
def dasboard_page():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return 'You are at the dashboard'
    
if __name__=="__main__":
    app.run(debug=True, host="localhost", port=8000 )                   

