from rogues_den import db
from flask_login import UserMixin
from sqlalchemy import Enum


class Users(db.Model, UserMixin):
    """
    Schema for the Users model
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    character_id = db.relationship('Character', backref='users', lazy=True)

    @property
    def is_authenticated(self):
        return True  # All users logged in are authenticated

    @property
    def is_anonymous(self):
        return False  # Regular users are not anonymous

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.username


class Character(db.Model):
    """
    Schema for the Character model
    """

    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(20), nullable=False)
    character_race = db.Column(Enum('Dragonborn', 'Dwarf', 'Elf', 'Gnome',
                                    'Half-Elf', 'Halfling',
                                    'Half-Orc', 'Human', 'Tiefling',
                                    name='character_types'),
                               nullable=False)
    character_class = db.Column(Enum('Barbarian', 'Bard', 'Cleric',
                                     'Druid', 'Fighter', 'Monk',
                                     'Paladin', 'Ranger', 'Rogue', 'Sorcerer',
                                     'Warlock', 'Wizard',
                                     name='character_classes'), nullable=False)
    character_level = db.Column(db.Integer, nullable=False)
    character_strength = db.Column(db.Integer, nullable=False)
    character_dexterity = db.Column(db.Integer, nullable=False)
    character_constitution = db.Column(db.Integer, nullable=False)
    character_intelligence = db.Column(db.Integer, nullable=False)
    character_wisdom = db.Column(db.Integer, nullable=False)
    character_charisma = db.Column(db.Integer, nullable=False)
    character_background = db.Column(db.Text, nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.character_name
