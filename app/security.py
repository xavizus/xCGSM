from flask import redirect, url_for
from flask_login import LoginManager
from app.models.users.models import User

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return redirect(url_for('login.login'))