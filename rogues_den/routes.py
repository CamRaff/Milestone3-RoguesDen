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

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/characters')
def characters():
    return render_template('characters.html')