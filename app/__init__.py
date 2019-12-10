from flask import Flask
from flask_bootstrap import Bootstrap
import os

from config import Config

from flask_pymongo import PyMongo,MongoClient
from flask_admin import Admin
from flask_admin.contrib.pymongo import ModelView

from .models import ProposalForm,ProposalView,UserForm,UserView

app = Flask(__name__, instance_relative_config=True)
Bootstrap(app)


app.config.from_object(Config)
app.config.from_pyfile('config.py')

admin = Admin(app)

mongo = PyMongo(app)

client = MongoClient(app.config['MONGO_URI'])
#client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'],27017)

db = client[app.config['MONGO_DBNAME']]
proposals = db["Proposal"]
#users    = db["users"]

admin.add_view(ProposalView(proposals))
#admin.add_view(UserView(users))


from . import views
