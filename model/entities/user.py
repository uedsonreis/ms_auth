from settings import db
from sqlalchemy.sql import func


user_role = db.Table(
    "users_roles", db.metadata,
    db.Column('user_id', db.ForeignKey('users.id'), primary_key=True),
    db.Column('role_id', db.ForeignKey('roles.id'), primary_key=True)
)


class User(db.Model, object):

    __tablename__ = 'users'

    id: int = db.Column(db.Integer(), primary_key=True)
    created = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    modified = db.Column(db.DateTime(timezone=True))
    modifier_user = db.Column(db.String(100))
    valid: bool = db.Column(db.Boolean(), nullable=False, default=True)

    username: str = db.Column(db.String(100), unique=True, nullable=False)
    password: str = db.Column(db.String(20))
    name: str = db.Column(db.String(100), nullable=False)
    admin: bool = db.Column(db.Boolean(), nullable=False, default=False)

    roles = db.relationship("Role", secondary=user_role)

    def __init__(self, id, name, username, password):
        self.id = id
        self.valid = True
        self.name = name
        self.username = username
        self.password = password
        self.admin = False
