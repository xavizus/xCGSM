from flask import current_app
from app.models.models import db
from sqlalchemy.sql import func
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
import bcrypt

roles = db.Table(
    'roles',
    db.Column(
        'user_id', db.Integer,
        db.ForeignKey('user.id'),
        primary_key=True
    ),
    db.Column(
        'role_id',
        db.Integer,
        db.ForeignKey('role.id'),
        primary_key=True
    )
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(80), nullable=False)
    created_date = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now()
    )
    updated_date = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    @property
    def password(self):
        raise AttributeError('password not readable')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.hashpw(
            password.encode('utf8'), bcrypt.gensalt()
        )

    def verify_password(self, password):
        return bcrypt.checkpw(password.encode('utf8'), self.password_hash.encode('utf8'))

    def __repr__(self):
        return f'<User {self.username}>'

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
    
    def generate_auth_token(self, expiration=600):
        s = Serializer(current_app.config.get('SECRET_KEY'), expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = User.query.get(data['id'])
        return user

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    users = db.relationship(
        "User",
        secondary=roles
    )
