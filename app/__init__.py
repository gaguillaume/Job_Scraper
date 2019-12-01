from flask import Flask
from flask_bootstrap import Bootstrap

from config import Config

app = Flask(__name__, instance_relative_config=True)
Bootstrap(app)

from . import views

app.config.from_object(Config)
app.config.from_pyfile('config.py')
