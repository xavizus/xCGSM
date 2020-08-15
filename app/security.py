from flask import redirect, url_for, request, jsonify
from flask_login import LoginManager
from app.models.users.models import User
import base64

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    if request.authorization:
        return jsonify(
            success=False,
            data={'login_required': True},
            message='Authorize please to access this page'
        ), 401
    return redirect(url_for('login.login', wantedUrl=request.full_path))


@login_manager.request_loader
def load_user_from_header(request):
    try:
        header_val = request.headers.get('Authorization')
        header_val = header_val.replace('Basic ', '', 1)
        header_val = base64.b64decode(header_val)
    except TypeError:
        return None
    except AttributeError:
        return None
    return User.verify_auth_token(header_val)
