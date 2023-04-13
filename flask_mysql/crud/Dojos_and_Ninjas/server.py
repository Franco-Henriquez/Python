from flask_app import app

# even if they are not being used within our server.py
# these two lines are what tells python to read the routes
# from both of these files.
from flask_app.controllers import dojos
from flask_app.controllers import ninjas


if __name__ == '__main__':
    app.run(debug=True)