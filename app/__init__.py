from flask import Flask
from flask_bootstrap import Bootstrap
import os
from config import Config

from flask_pymongo import PyMongo,MongoClient
from flask_admin import Admin
from flask_admin.contrib.pymongo import ModelView
from elasticsearch import Elasticsearch

app = Flask(__name__, instance_relative_config=True)
Bootstrap(app)

#es = Elasticsearch([{'host':'elasticsearch','port':9200}])
#es.indices.create(index='annonces')



app.config.from_object(Config)
app.config.from_pyfile('config.py')

MONGO_URI = app.config["MONGO_URI"]


admin = Admin(app)

mongo = PyMongo(app)

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
