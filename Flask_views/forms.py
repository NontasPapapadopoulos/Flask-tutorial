from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, StringField
from wtforms.fields.simple import SubmitField


class AddForm(FlaskForm):
    name = StringField('Name of Puppy')
    submit = SubmitField('Add Puppy')


class DelForm(FlaskForm):
    id = IntegerField("Id Number of Puppy to Remove: ")
    submit = SubmitField("Remove Puppy")


class AddOwner(FlaskForm):
    name = StringField('Name of Owner')
    puppyId = IntegerField('Id of Puppy')
    submit = SubmitField('Add Owner')


class DeleteAll(FlaskForm):
    submit = SubmitField('Delete All')
