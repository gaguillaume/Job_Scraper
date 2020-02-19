from flask import Flask
from flask_bootstrap import Bootstrap

from dash import Dash 
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

import os
from config import Config

from flask_pymongo import PyMongo,MongoClient
from flask_admin import Admin
from flask_admin.contrib.pymongo import ModelView
from elasticsearch import Elasticsearch

server = Flask(__name__, instance_relative_config = True) 

app_dash = Dash(__name__, server = server, routes_pathname_prefix='/dash/', 
				external_stylesheets=[dbc.themes.BOOTSTRAP])

Bootstrap(server)

#es = Elasticsearch([{'host':'elasticsearch','port':9200}])
#es.indices.create(index='annonces')



server.config.from_object(Config)
server.config.from_pyfile('config.py')

MONGO_URI = server.config["MONGO_URI"]


admin = Admin(server)

mongo = PyMongo(server)

client =  MongoClient(MONGO_URI)
#client = MongoClient('mongodb',27017)
#client = MongoClient('mongodb://mongodb:27017/')
#client = MongoClient(app.config['MONGO_URI'])
#client = MongoClient(os.environ.get['mongo_db'],27017)



db = client["mongodb"]
proposals = db["Proposal"]
indeed = db["Indeed"]
#users    = db["users"]

from .models import ProposalForm,ProposalView,UserForm,UserView,IndeedForm,IndeedView


admin.add_view(IndeedView(indeed))


#admin.add_view(UserView(users))


from . import views
