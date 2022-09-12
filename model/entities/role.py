from settings import db
from sqlalchemy.sql import func


class Role(db.Model, object):

    __tablename__ = 'roles'

    id: int = db.Column(db.Integer(), primary_key=True)
    created = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    modified = db.Column(db.DateTime(timezone=True))
    modifier_user = db.Column(db.String(100))
    valid: bool = db.Column(db.Boolean(), nullable=False, default=True)

    name: str = db.Column(db.String(100), nullable=False)
    description: str = db.Column(db.String(255))

    def __init__(self, id, name, description):
        self.id = id
        self.valid = True
        self.name = name
        self.description = description
