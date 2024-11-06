from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from rogues_den import app, db
from rogues_den.models import Users, Character


routes = Blueprint('routes', __name__)


@app.route('/')
def home():
    return render_template('base.html')


# @app.route('/login')
# def login():
#     return render_template('login.html')

@app.route('/profile', methods=["GET"])
@login_required
def profile():

    users = Users.query.get(current_user.id)

    return render_template('profile.html', users=users)

@app.route('/characters')
@login_required
def characters():

    return render_template('characters.html')