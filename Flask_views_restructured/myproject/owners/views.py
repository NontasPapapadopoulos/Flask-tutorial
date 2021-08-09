from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import AddOwner


owners_blueprint = Blueprint(
    'owners', __name__, template_folder='templates/owners')


@owners_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    form = AddOwner()

    if form.validate_on_submit():
        # grab details from the form
        name = form.name.data
        puppyId = form.puppyId.data

        # Create an owner instance
        owner = Owner(name, puppyId)

        db.session.add(owner)
        db.session.commit()

        return redirect(url_for('puppies.list'))

    return render_template('owner.html', form=form)
