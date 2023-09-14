from flask_app import app
from flask import render_template, session, redirect,request,url_for,make_response

#ruta proveedor
@app.route("/")
def index():
    return render_template("index.html")