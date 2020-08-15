from flask import Blueprint, render_template, redirect, url_for
import app.models.users.models as Users
from app.models.models import db
from flask_login import login_required, login_user, logout_user

login_bp = Blueprint('login', __name__)


@login_bp.route('/')
@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    user = db.session.query(Users.User)\
        .filter(Users.User.username == "admin1")\
        .first()
    if user:
        if user.verify_password('123456789abc'):
            login_user(user)
    return render_template('login.html')


@login_bp.route('/create')
def createUser():
    try:
        user1 = Users.User(
            username="admin1",
            email="admin1@localhost",
            password="123456789abc"
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
    except Exception as error:
        print(error)

    return "OK", 200


@login_bp.route('/logout')
@login_required
def logoutUser():
    logout_user()
    return redirect(url_for('login.login'))
