from flask_admin.contrib.pymongo import ModelView
from flask_wtf import FlaskForm
from wtforms import TextField,BooleanField,SubmitField,StringField
from wtforms.validators import DataRequired
from flask_admin.contrib.pymongo.filters import BasePyMongoFilter
from . import indeed


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
    site = TextField('Site')
    job_title = TextField('Job Title')
    company = TextField('Company')
    location = TextField('Location')
    salary = TextField('Salary')
    summary = TextField('Summary')
    link_url = TextField('Link_url')
    crawl_url = TextField('Crawl_url')

class FilterSiteIndeed(BasePyMongoFilter):
    def apply(self, query,value):
        if value==1:

            return query.filter(self.column == "Indeed")
        else:
            return query.filter(self.column == "Monster")

    def operation(self):
        return 'Indeed'

class IndeedView(ModelView):

    column_list = ('site','job_title','company','location','salary','summary','link_url','crawl_url')
    column_filters = [FilterSiteIndeed(column = indeed.site,name = 'site')]
    form = IndeedForm

class FeaturesForm(FlaskForm):
    what = StringField("What",validators=[DataRequired()], render_kw={"placeholder": "What"})
    where = StringField("Where",validators=[DataRequired()], render_kw={"placeholder": "Where"})
    submit = SubmitField("Submit", render_kw={"placeholder": "Submit"})


class FilterForm(FlaskForm):
    dreamt_job = StringField("What",validators=[DataRequired()], render_kw={"placeholder": "What job are you dreaming about ?"})
    submit = SubmitField("Submit", render_kw={"placeholder": "Submit"})
