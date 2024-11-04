from flask import render_template
from rogues_den import app, db
from rogues_den.models import User, Character


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/characters')
def characters():
    return render_template('characters.html')