from flask_sqlalchemy import SQLAlchemy, Model
from lib_ms_api.abstract_repository import AbstractRepository

from model.entities.role import Role, db


class __RoleRepository(AbstractRepository):

    def get_model(self) -> Model:
        return Role

    def get_database(self) -> SQLAlchemy:
        return db

    def get_by_name(self, _name: str):
        return self.get_model().query.filter_by(name=_name).first()


roleRepository = __RoleRepository()
