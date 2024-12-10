from flask import Flask
from models import db, Producto

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://u570313410_alan:TokkenCBA123@srv1076.hstgr.io/u570313410_tokkenback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    productos = [
        Producto(nombre='Producto 1', ean='123', descripcion='Descripción del producto 1', precio=10.99, stock=100, image_path='ruta/imagen1.jpg'),
        Producto(nombre='Producto 2', ean='345', descripcion='Descripción del producto 2', precio=20.99, stock=200, image_path='ruta/imagen2.jpg'),
        Producto(nombre='Producto 3', ean='789', descripcion='Descripción del producto 3', precio=30.99, stock=300, image_path='ruta/imagen3.jpg')
    ]

    db.session.bulk_save_objects(productos)
    db.session.commit()

    print("Productos de ejemplo insertados exitosamente")