from flask import Flask, request, jsonify, url_for
from flask import render_template
import sys
sys.path.append("src")
from View.Web import liquidation_app

# Crear la aplicación Flask
app = Flask(__name__)

# Establecer la clave secreta para las sesiones y mensajes flash
app.config['SECRET_KEY'] = 'practicaflask'  # Cambia esto por una clave secreta real

# Registrar el blueprint
app.register_blueprint(liquidation_app.main_bp)

if __name__ == '__main__':
    app.run(debug=True)
