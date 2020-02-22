from flask import render_template,request,redirect,url_for,render_template_string,flash
from . import app_dash, server,proposals,mongo,db,MONGO_URI,indeed
from .models import FeaturesForm,FilterForm

import json
import requests

import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


@server.route('/')
def base():
    return render_template('index.html')


@server.route('/scraper',methods=['GET','POST'])
def scraper():
    form_indeed = FeaturesForm()
    form_monster = FeaturesForm()
    result = "No data scraped (Indeed) - Here will be the preview of the json data"
    result2 = "No data scraped (Monster) - Here will be the preview of the json data"

    if request.method == 'POST':
        if form_indeed.validate_on_submit():
            what = form_indeed.what.data
            where = form_indeed.where.data
            response = requests.get("http://scraper:9080/crawl.json?spider_name=indeed&url=https://www.indeed.fr/jobs?q={0}&l={1}&sort=date&start=00&max_requests=5".format(what,where))
            data = json.loads(response.text)
            result = '\n'.join('Job Indeed : {} - Salaire {}   // '.format(item['job_title'], item['salary']) for item in data['items'])
        if form_monster.validate_on_submit():
            what2 = form_monster.what.data
            where2 = form_monster.where.data
            response2 = requests.get("http://scraper:9080/crawl.json?spider_name=monster&url=https://www.monster.fr/emploi/recherche/?q={0}&where={1}&page=5".format(what2,where2))
            data2 = json.loads(response2.text)
            result2 = '\n'.join('Job Monster : {} // '.format(item['job_title']) for item in data2['items'])
    return render_template("scraper.html",form_indeed=form_indeed,form_monster=form_monster,result=result,result2=result2)



@server.route('/search',methods=['GET','POST'])
def makeResearch():
    form = FilterForm()
    dreamt_job = form.dreamt_job.data
    files = indeed.find({"job_title":str(dreamt_job)})
    data = []
    for file in files:
        data.append(file['job_title'])

    return render_template("search.html",form=form,data=data)


#@app.route('/admin') existe via l'admin


navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            color = "info",
            label="Contact",
            children=[
                dbc.DropdownMenuItem("Franck Deturche-Dura",href='https://www.linkedin.com/in/franck-deturche-dura'),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Guillaume Gay", href='https://www.linkedin.com/in/guillaumegay/'),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Yasmine Djemame",href='https://www.linkedin.com/in/yasmine-djemame-382314198/'),
            ],
        ),
    ],
    brand="Job advertisements scrapping",
    brand_href="#",
    sticky="top",
)

what_input = dbc.FormGroup(
    [
        dbc.Label("What", width=2),
        dbc.Col(
            dbc.Input(
                type="text", id="what", placeholder="Intitulé du Job"
            ),
            width=10,
        ),
    ],
    row=True,
)

where_input = dbc.FormGroup(
    [
        dbc.Label("Where", width=2),
        dbc.Col(
            dbc.Input(
                type="text", id="where", placeholder="Secteur",
            ),
            width=10,
        ),
    ],
    row=True,
)

submit_button =  dbc.Button("Rechercher", color="secondary", className="mr-1", id="button_spend")


table_header = [
    html.Thead(html.Tr([html.Th("Job"), html.Th("Compagnie"), html.Th("Location"), html.Th("Salary"),html.Th("Summary"),html.Th("Lien"), html.Th("Site")]))
]


table_body = [html.Tbody(id='formulaire')]


body = dbc.Container(
    [

        dbc.Row([dbc.Form([what_input, where_input, submit_button]) ]),
        html.Br(), html.Br(),
        dbc.Row([dbc.Table( table_header + table_body, bordered=True, dark=True, hover=True, responsive=True,
            striped=True)])

    ],
    className="mt-4",
)

app_dash.layout = html.Div([navbar,body])


@app_dash.callback(Output('formulaire', 'children'),
    [Input('what', 'value'), Input('where', 'value'), Input("button_spend","n_clicks")])

def display_table(what, where, n):
    listrows = []

    if n != None:

        response = requests.get("http://scraper:9080/crawl.json?spider_name=indeed&url=https://www.indeed.fr/jobs?q={0}&l={1}&sort=date&start=00&max_requests=5".format(what, where))
        data = json.loads(response.text)

        for item in data['items']:
            listrows.append(html.Tr([html.Td(item['job_title']), html.Td(item['company']), html.Td(item['location']), html.Td(item['salary']), html.Td(item['summary']),html.Td(item['crawl_url']), html.Td(item['site'])]))


        response2 = requests.get("http://scraper:9080/crawl.json?spider_name=monster&url=https://www.monster.fr/emploi/recherche/?q={0}&where={1}&page=5".format(what,where))
        data2 = json.loads(response2.text)

        for item in data2['items']:
            listrows.append(html.Tr([html.Td(item['job_title']), html.Td(item['company']), html.Td(item['location']), html.Td(item['salary']), html.Td(item['summary']),html.Td(item['crawl_url']), html.Td(item['site'])]))


        return listrows
