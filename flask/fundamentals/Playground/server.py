from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/')
def box_main():
    return render_template("index.html",boxes=3,color="blue")

@app.route('/play/<int:num_of_boxes>/')
def box_number(num_of_boxes):
    return render_template("index.html",boxes=num_of_boxes,color="blue")

@app.route('/play/<int:num_of_boxes>/<string:color>/')
def box_number_color(num_of_boxes,color):
    return render_template("index.html",boxes=num_of_boxes,color=color)

if __name__=="__main__":
    app.run(debug=True, host="localhost", port=8800 )          