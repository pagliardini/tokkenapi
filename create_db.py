from flask import Flask
from models import db
import json
from pathlib import Path

app = Flask(__name__)

# Cargar configuración desde el archivo JSON
config_path = Path(__file__).parent / 'conexion.json'
with open(config_path) as config_file:
    config = json.load(config_file)

app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['SQLALCHEMY_TRACK_MODIFICATIONS']

db.init_app(app)

with app.app_context():
    db.create_all()
    print("Base de datos y tablas creadas exitosamente")