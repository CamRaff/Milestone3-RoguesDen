from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from rogues_den import app, db
from rogues_den.models import Users, Character


routes = Blueprint('routes', __name__)


@app.route('/home')
def home():
    return render_template('base.html')


@app.route('/profile', methods=["GET"])
@login_required
def profile():

    users = Users.query.get(current_user.id)
    return render_template('profile.html', users=users)


@app.route('/characters')
@login_required
def characters():
    # extracts character data from the database
    characters = Character.query.filter_by(users_id=current_user.id)
    return render_template('characters.html', characters=characters)


@app.route('/add_character', methods=["GET", "POST"])
@login_required
def add_character():

    if request.method == "POST":
        try:
            # extract form data from the database
            character_name=request.form.get("character_name")
            character_race=request.form.get("character_race")
            character_class=request.form.get("character_class")
            character_level=int(request.form.get("character_level") or 1)
            character_strength=int(request.form.get("character_strength") or 0)
            character_dexterity=int(request.form.get("character_dexterity") or 0)
            character_constitution=int(request.form.get("character_constitution") or 0)
            character_intelligence=int(request.form.get("character_intelligence") or 0)
            character_wisdom=int(request.form.get("character_wisdom") or 0)
            character_charisma=int(request.form.get("character_charisma") or 0)
            character_background=request.form.get("character_background")

            if not character_name or not character_race or not character_class:
                flash("Name, Race and Class are required fields!", category="error")
                return render_template('add_character.html')

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

            try:
                db.session.add(new_character)
                db.session.commit()
                flash("New character created!", category="success")
                return redirect(url_for('characters'))
            except Exception as e:
                db.session.rollback()
                flash(f"Error creating character: {e}", category="error")

        except ValueError:
            flash("Please ensure all numeric fields contain valid inputs.", category="error")

    races = [race for race in Character.__table__.columns.character_race.type.enums]
    classes = [chcls for chcls in Character.__table__.columns.character_class.type.enums]
    return render_template('add_character.html', races=races, classes=classes)


@app.route('/edit_character/<int:character_id>', methods=["GET", "POST"])
@login_required
def edit_character(character_id):

    character = Character.query.get_or_404(character_id)

    if request.method == "POST":
        character_level=int(request.form.get("character_level") or 1)
        character_strength=int(request.form.get("character_strength") or 0)
        character_dexterity=int(request.form.get("character_dexterity") or 0)
        character_constitution=int(request.form.get("character_constitution") or 0)
        character_intelligence=int(request.form.get("character_intelligence") or 0)
        character_wisdom=int(request.form.get("character_wisdom") or 0)
        character_charisma=int(request.form.get("character_charisma") or 0)
        character_background=request.form.get("character_background")

        character.character_level=character_level
        character.character_strength=character_strength
        character.character_dexterity=character_dexterity
        character.character_constitution=character_constitution
        character.character_intelligence=character_intelligence
        character.character_wisdom=character_wisdom
        character.character_charisma=character_charisma
        character.character_background=character_background

        db.session.commit()
        flash("Character updated!", category="success")
        return redirect(url_for('characters'))

    return render_template('edit_character.html', character=character)


@app.route('/character_view/<int:character_id>', methods=["GET", "POST"])
@login_required
def character_view(character_id):
    # extracts character data from the database
    character = Character.query.get_or_404(character_id)
    return render_template('character_view.html', character=character)


@app.route('/delete_character/<int:character_id>')
def delete_character(character_id):
    character = Character.query.get_or_404(character_id)
    db.session.delete(character)
    db.session.commit()
    return redirect(url_for('characters'))


if __name__ == '__main__':
    app.run(debug=False)


@app.route('/force-500')
def force_500_error():
    # Raise an exception to trigger a 500 error
    raise Exception("Intentional 500 error for testing purposes")