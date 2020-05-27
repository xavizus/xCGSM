from flask import Flask
from config import config
from app.models.models import db, migrate
from app.security import login_manager

# Blueprints
from app.blueprints.login.login_blueprint import login_bp


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
    setupRoutes(app)
    return app


def setupRoutes(app):
    app.register_blueprint(login_bp)
