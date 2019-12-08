from flask import Flask
from flask_bootstrap import Bootstrap

from config import Config

from flask_pymongo import PyMongo,MongoClient

app = Flask(__name__, instance_relative_config=True)
Bootstrap(app)


app.config.from_object(Config)
app.config.from_pyfile('config.py')

mongo = PyMongo(app)

client = MongoClient(app.config['MONGO_URI'])

db = client[app.config['MONGO_DBNAME']]
proposals = db["Proposal"]


from . import views
