from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from productos import productos_bp
from models import db
from config import photos, configure_app
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://u570313410_alan:TokkenCBA123@srv1076.hstgr.io/u570313410_tokkenback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join('static', 'uploads')

# Agregar configuración de pool_pre_ping para reconexión automática
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_pre_ping': True,   # Verificar si la conexión está activa antes de usarla
    'pool_recycle': 2800   # Reciclar conexiones inactivas
}

configure_app(app)
db.init_app(app)

app.register_blueprint(productos_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
