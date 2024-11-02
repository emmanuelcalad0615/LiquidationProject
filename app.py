from flask import Flask, request, jsonify , url_for
from flask import render_template
import sys
sys.path.append("src")
from View.Web import liquidation_app

app = Flask(__name__)
app.register_blueprint( liquidation_app.blueprint )

if __name__=='__main__':
   app.run( debug=True )