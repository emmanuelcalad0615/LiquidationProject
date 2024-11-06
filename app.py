""" 
Import the necessary modules from Flask, request, jsonify, and url_for, along with render_template for rendering HTML templates.
Also, sys is imported to allow manipulation of the system path, which enables us to import custom modules from a specific directory.
"""
from flask import Flask, request, jsonify, url_for
from flask import render_template
import sys

""" 
Add the "src" directory to the system path so that we can import custom modules from it. 
This allows us to import the `liquidation_app` blueprint from the `View.Web` module.
"""
sys.path.append("src")
from View.Web import liquidation_app

""" 
Create an instance of the Flask application. 
This object will handle routing, request handling, and response generation for the web application.
"""
app = Flask(__name__)

""" 
Set the secret key for the application. 
This key is used for securely signing cookies, sessions, and other security-related operations. 
In a real production app, it is recommended to use a more secure and random key.
"""
app.config['SECRET_KEY'] = 'practicaflask'  # Change this to a real secret key for production use

""" 
Register the blueprint `liquidation_app.main_bp` with the Flask app. 
A blueprint in Flask is a way to organize routes and handlers into separate modules. 
In this case, the `main_bp` blueprint from the `liquidation_app` module is registered, allowing routes and views defined in that blueprint to be part of the app.
"""
app.register_blueprint(liquidation_app.main_bp)

""" 
Start the Flask application in debug mode. 
This means that the server will automatically reload when changes are made to the code, 
and any errors will be shown in the browser for easier debugging.
"""
if __name__ == '__main__':
    app.run(debug=True)
