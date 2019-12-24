from flask import render_template,request,redirect,url_for,render_template_string,flash
from . import app,proposals,mongo,db,MONGO_URI
from .models import FeaturesForm

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
        response = requests.get("http://scraper:9080/crawl.json?spider_name=indeed2&url=https://www.indeed.fr/jobs?q={0}&l={1}&sort=date&start=00&max_requests=5".format(what,where))
        data = json.loads(response.text)
        result = '\n'.join('Job : {}</b> - Salaire {}   // '.format(item['job_title'], item['salary']) for item in data['items'])

    return render_template("scraper.html",form=form,result=result)




#@app.route('/admin') existe via l'admin
