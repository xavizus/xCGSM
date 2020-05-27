from app.models.models import db
from sqlalchemy.sql import func

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
    pw_hash = db.Column(db.String(80), nullable=False)
    created_date = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now()
    )
    updated_date = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    users = db.relationship(
        "User",
        secondary=roles
    )
