from flask import render_template,request,redirect,url_for,render_template_string,flash
from . import app,proposals,mongo,db,MONGO_URI

import json
import requests



@app.route('/')
def base():
    return render_template('index.html')

@app.route('/indeed')
def show_proposals():
    params = {'spider_name':'indeed2','start_requests':True}
    response = requests.get("http://scraper:9080/crawl.json?spider_name=indeed2&url=https://www.indeed.fr/jobs?q=Informatique&l=Paris&sort=date&start=00")
    data = json.loads(response.text)
    result = '\n'.join('<p><b>{}</b> - {}</p>'.format(item['author'], item['text']) for item in data['items'])
    return render_template("indeed.html",result=result)



@app.route('/db')
def show_db():

    #nombre_data = str(mongo.db.Proposal.count())
    #nombre_data = mongo.db.Proposal.find({"job":"Greviste"})
    #nombre_data = list(db["Proposal"].find())
    nombre_data = proposals.find_one_or_404()
    #nombre_data = db.Proposal.find_one_or_404()
    #nombre_data = nombre_data.count(True)
    #nombre_data = nombre_data.count()
    #nombre_data = nombre_data.count(True)
    #nombre_data = str(type(proposals))
    #results = mongo.db.Proposal.find()
    #nombre_data = str(results.count(True))
    #nombre_data = str(MONGO_URI)
    #nombre_data = str(type(proposals))

    if nombre_data != "":
        print(nombre_data)
        return render_template("db.html",nombre_data=nombre_data)
    else :
        return render_template_string("Error")

#@app.route('/admin') existe via l'admin
