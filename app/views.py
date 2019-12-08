from flask import render_template,request,redirect,url_for,render_template_string,flash
from . import app,mongo,proposals

@app.route('/')
def base():
    return render_template('index.html')

@app.route('/db')
def show_db():
    #nombre_data = str(mongo.db.Proposal.count())
    nombre_data = proposals.count()
    if nombre_data != "":
        print(nombre_data)
        return render_template("db.html",nombre_data=nombre_data)
    else :
        return render_template_string("Error")
