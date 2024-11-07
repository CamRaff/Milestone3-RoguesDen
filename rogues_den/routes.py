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


@app.route('/add_character', methods=["GET", "POST"])
@login_required
def add_character():

    if request.method == "POST":
        # extract form data from the database
        character_name=request.form.get("characte_name"),
        character_race=request.form.get("character_race"),
        character_class=request.form.get("character_class"),
        character_level=int(request.form.get("character_level")),
        character_strength=int(request.form.get("character_strength")),
        character_dexterity=int(request.form.get("character_dexterity")),
        character_constitution=int(request.form.get("character_constitution")),
        character_intelligence=int(request.form.get("character_intelligence")),
        character_wisdom=int(request.form.get("character_wisdom")),
        character_charisma=int(request.form.get("character_charisma")),
        character_background=request.form.get("character_background")

        new_character= Character(
            character_name=character_name,
            character_race=character_race,
            character_class=character_class,
            character_level=character_level,
            character_strength=character_strength,
            character_dexterity=character_dexterity,
            character_constitution=character_constitution,
            character_intelligence=character_intelligence,
            character_wisdom=character_wisdom,
            character_charisma=character_charisma,
            character_background=character_background,
            users_id=current_user.id
        )

        db.session.add(new_character)
        db.session.commit()

        flash("New character created!", category="success")

    return render_template('add_character.html')