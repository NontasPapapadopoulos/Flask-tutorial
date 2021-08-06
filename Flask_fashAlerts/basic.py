from flask import Flask,  render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField, TextField, TextAreaField, SubmitField)
from wtforms.fields.core import SelectField


from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'kmykey'
app.config


class SimpleForm(FlaskForm):
    submit = SubmitField('Submit')
    breed = StringField('What breed are you?')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()

    if form.validate_on_submit():
        flash('Your breed is ' + form.breed.data)

        return redirect(url_for('index'))

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
