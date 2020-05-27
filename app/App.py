from flask import Flask
from config import config
from app.models.models import db, migrate
from app.security import login_manager

# Blueprints
from app.blueprints.login.login_blueprint import login_bp
from app.blueprints.admin.admin_blueprint import admin_bp


def createApp():
    app = Flask(
        __name__,
        static_folder='static',
        template_folder='templates'
    )
    app.config.from_object(config)
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    initJinja(app)
    setupRoutes(app)
    return app


def initJinja(app):
    app.jinja_env.globals['applicationData'] = {
        "appName": app.config.get('APP_NAME')
    }


def setupRoutes(app):
    app.register_blueprint(login_bp, url_prefix='')
    app.register_blueprint(admin_bp, url_prefix='/admin')
