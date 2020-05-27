from flask import Blueprint, render_template
# import app.models.users.models as Users
# from app.models.models import db
from flask_login import login_required, current_user

admin_bp = Blueprint('admin', __name__)


@admin_bp.before_request
@login_required
def before_request():
    pass


@admin_bp.route('/')
def dashboard():
    data = {
        "contentTitle": "This is a Title",
        "subContentTitle": "SubContentTitle",
        "cardTitle": "This is cardTitle",
        "username":  current_user.username
    }
    return render_template('dashboard.html', data=data)