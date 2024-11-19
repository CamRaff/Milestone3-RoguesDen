import os
from flask import Flask, Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
if os.path.exists('env.py'):
    import env


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

if os.environ.get("DEVELOPMENT") == "True":
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
else:
    uri = os.environ.get('DATABASE_URL')
    if uri.startswith('postgres://'):
        uri = uri.replace('postgres://', 'postgresql://', 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = uri

db = SQLAlchemy(app)

# importing the routes for the app traversal
from .routes import routes  # noqa # needed here for app initialization
# importing the auth routes for login/register/log out
from .auth import auth  # noqa # needed here for app initialization
# importing the Users model for authentication
from .models import Users  # noqa #needed here for app initialization

app.register_blueprint(routes)
app.register_blueprint(auth)

errors = Blueprint('errors', __name__)
app.register_blueprint(errors)

# Initializes the LoginManager for use in the app
login_manager = LoginManager(app)

# Set the login view for unauthorized access
login_manager.login_view = 'auth.login'
# login_manager.login_message_category = 'info' (optional)


# Initialize user_loader to reload user from ID stored in session
@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))


# Global 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Global 500 error handler
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# Global 401 error handler
@app.errorhandler(401)
def unauthorized_error(e):
    return render_template('401.html'), 401
