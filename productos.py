from flask import Blueprint, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_uploads import UploadSet, IMAGES, configure_uploads
from wtforms import StringField, TextAreaField, DecimalField, IntegerField, FileField, SubmitField
from wtforms.validators import DataRequired
from models import db, Producto
from config import photos

productos_bp = Blueprint('productos', __name__)

class ProductoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción')
    ean = StringField('EAN', validators=[DataRequired()])
    precio = DecimalField('Precio', validators=[DataRequired()])
    stock = IntegerField('Stock', validators=[DataRequired()])
    image = FileField('Imagen', validators=[DataRequired()])
    submit = SubmitField('Crear Producto')

@productos_bp.route('/productos')
def productos():
    productos = Producto.query.all()
    return render_template('productos.html', productos=productos)

@productos_bp.route('/productos/crear', methods=['GET', 'POST'])
def crear_producto():
    form = ProductoForm()
    if form.validate_on_submit():
        filename = photos.save(form.image.data)
        ean = form.ean.data
        nombre = form.nombre.data
        descripcion = form.descripcion.data
        precio = form.precio.data
        stock = form.stock.data
        image_path = filename

        nuevo_producto = Producto(
            ean=ean,
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            image_path=image_path
        )

        db.session.add(nuevo_producto)
        db.session.commit()

        return redirect(url_for('productos.productos'))
    return render_template('crear_producto.html', form=form)