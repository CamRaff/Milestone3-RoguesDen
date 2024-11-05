import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
if os.path.exists('env.py'):
    import env


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')


db = SQLAlchemy(app)

from .routes import routes # importing the routes for the app traversal
from .auth import auth # importing the auth routes for login/register/log out
from .models import Users

app.register_blueprint(routes)
app.register_blueprint(auth)
# app.register_blueprint(errors)

# Initializes the LoginManager for use in the app
login_manager = LoginManager(app)

# Set the login view for unauthorized access
login_manager.login_view = 'auth.login'
# login_manager.login_message_category = 'info'  # Flash message category (optional)

# Initialize user_loader to reload user from ID stored in session
@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))
