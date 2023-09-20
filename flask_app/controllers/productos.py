from flask_app import app
from flask import render_template, session, redirect,request,url_for,make_response

#ruta productos
@app.route("/productos")
def registrarproductos():
    return render_template("registros_productos.html")