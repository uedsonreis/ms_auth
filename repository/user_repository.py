from flask_sqlalchemy import SQLAlchemy, Model
from lib_ms_api.abstract_repository import AbstractRepository

from model.entities.user import User, db


class __UserRepository(AbstractRepository):

    def get_model(self) -> Model:
        return User

    def get_database(self) -> SQLAlchemy:
        return db

    def get_by_username(self, _username: str):
        return self.get_model().query.filter_by(username=_username).first()


userRepository = __UserRepository()
