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
    form = FeaturesForm()
    result = "No data scraped - Here will be the preview of the json data"
    if request.method == 'POST':

        what = form.what.data
        where = form.where.data
        response = requests.get("http://scraper:9080/crawl.json?spider_name=indeed&url=https://www.indeed.fr/jobs?q={0}&l={1}&sort=date&start=00&max_requests=5".format(what,where))
        data = json.loads(response.text)
        result = '\n'.join('Job : {}</b> - Salaire {}   // '.format(item['job_title'], item['salary']) for item in data['items'])
    return render_template("scraper.html",form=form,result=result)

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
