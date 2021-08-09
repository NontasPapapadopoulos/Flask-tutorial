from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, StringField
from wtforms.fields.simple import SubmitField


class AddOwner(FlaskForm):
    name = StringField('Name of Owner')
    puppyId = IntegerField('Id of Puppy')
    submit = SubmitField('Add Owner')
