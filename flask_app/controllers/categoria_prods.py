from flask_app import app
from flask import render_template, session, redirect,request,url_for,make_response

#ruta principal
@app.route("/categoria_prods")
def registrarcategoriaprods():
    return render_template("categoria_prod.html")