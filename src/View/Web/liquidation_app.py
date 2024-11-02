from flask import Blueprint, render_template, request
blueprint = Blueprint( "liquidation_app", __name__, template_folder= "templates" )
import sys
sys.path.append("src")
from Controller.ControladorUsuarios import EmployeeController
from Logic import Compensation, employee, Liquidation

@blueprint.route("/")
def Home():
   return render_template('index.html')

@blueprint.route("/ingresar-informacion")
def ingresar_informacion():
   return render_template("form.html")
   


