from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    ean = db.Column(db.String(50) , nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text)
    subcategoria_id = db.Column(db.Integer, db.ForeignKey('subcategorias.id'), nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    image_path = db.Column(db.String(255))
    creado = db.Column(db.DateTime, default=db.func.current_timestamp())


class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    subcategorias = db.relationship('Subcategoria', backref='categoria', lazy=True)

class Subcategoria(db.Model):
    __tablename__ = 'subcategorias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    productos = db.relationship('Producto', backref='subcategoria', lazy=True)