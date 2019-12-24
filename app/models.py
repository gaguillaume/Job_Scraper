from flask_admin.contrib.pymongo import ModelView
from flask_wtf import FlaskForm
from wtforms import TextField,BooleanField,SubmitField,StringField
from wtforms.validators import DataRequired


class ProposalForm(FlaskForm):
    name = TextField('Job')
    lastname = TextField('Salaire')

class ProposalView(ModelView):
    column_list=('job','salaire')
    form = ProposalForm

class UserForm(FlaskForm):
    name = TextField('User')
    admin = TextField('Password')

class UserView(ModelView):
    column_list=('user','pwd')
    form = UserForm

class IndeedForm(FlaskForm):
    job_title = TextField('Job Title')
    company = TextField('Company')
    location = TextField('Location')
    salary = TextField('Salary')
    summary = TextField('Summary')
    link_url = TextField('Link_url')
    crawl_url = TextField('Crawl_url')

class IndeedView(ModelView):
    column_list = ('job_title','company','location','salary','summary','link_url','crawl_url')
    form = IndeedForm

class FeaturesForm(FlaskForm):
    what = StringField("What",validators=[DataRequired()], render_kw={"placeholder": "What"})
    where = StringField("Where",validators=[DataRequired()], render_kw={"placeholder": "Where"})
    submit = SubmitField("Submit", render_kw={"placeholder": "Submit"})
