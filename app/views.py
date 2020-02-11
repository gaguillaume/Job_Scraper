from flask import render_template,request,redirect,url_for,render_template_string,flash
from . import app,proposals,mongo,db,MONGO_URI,indeed
from .models import FeaturesForm,FilterForm

import json
import requests



@app.route('/')
def base():
    return render_template('index.html')


@app.route('/scraper',methods=['GET','POST'])
def scraper():
    form_indeed = FeaturesForm()
    form_monster = FeaturesForm()
    result = "No data scraped (Indeed) - Here will be the preview of the json data"
    result2 = "No data scraped (Monster) - Here will be the preview of the json data"

    if request.method == 'POST':

        what = form_indeed.what.data
        where = form_indeed.where.data
        response = requests.get("http://scraper:9080/crawl.json?spider_name=indeed&url=https://www.indeed.fr/jobs?q={0}&l={1}&sort=date&start=00&max_requests=5".format(what,where))
        data = json.loads(response.text)
        result = '\n'.join('Job Indeed : {}</b> - Salaire {}   // '.format(item['job_title'], item['salary']) for item in data['items'])

        what2 = form_monster.what.data
        where2 = form_monster.where.data
        response2 = requests.get("http://scraper:9080/crawl.json?spider_name=monster&url=https://www.monster.fr/emploi/recherche/?q={0}&where={1}&page=5".format(what2,where2))
        data2 = json.loads(response2.text)
        result2 = '\n'.join('Job Monster : {}</b> // '.format(item['job_title']) for item in data2['items'])
    return render_template("scraper.html",form_indeed=form_indeed,form_monster=form_monster,result=result,result2=result2)

@app.route('/search',methods=['GET','POST'])
def makeResearch():
    form = FilterForm()
    dreamt_job = form.dreamt_job.data
    files = indeed.find({"job_title":str(dreamt_job)})
    data = []
    for file in files:
        data.append(file['job_title'])

    return render_template("search.html",form=form,data=data)


#@app.route('/admin') existe via l'admin
