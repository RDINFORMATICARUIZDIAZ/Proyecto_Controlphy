from flask_app import app
from flask import render_template, session, redirect,request,url_for,make_response

#ruta principal
@app.route("/contactos")
def registrarcontactos():
    return render_template("registrar_contactos.html")