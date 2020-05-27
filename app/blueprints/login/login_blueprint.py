from flask import Blueprint, render_template, redirect, url_for
import app.models.users.models as Users
from app.models.models import db
from flask_login import login_required, login_user, logout_user

login_bp = Blueprint('login', __name__)


@login_bp.route('/')
@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    admin = db.session.query(Users.User)\
        .filter(Users.User.id == 1)\
        .first()
    if admin:
        login_user(admin)
    return render_template('login.html')


@login_bp.route('/create')
@login_required
def createUser():
    user1 = Users.User(
        username="admin",
        email="admin@localhost",
        pw_hash="123456789abc"
    )
    # Creates new role
    # role = Users.Role(name="admin")

    # Use existing role to assign to user
    role = db.session.query(Users.Role)\
        .filter(Users.Role.name == 'admin')\
        .first()
    role.users.append(user1)
    db.session.add(role)
    db.session.commit()

    return "OK", 200


@login_bp.route('/logout')
@login_required
def logoutUser():
    logout_user()
    return redirect(url_for('login.login'))
