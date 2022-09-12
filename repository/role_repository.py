from model.entities.role import Role, db
from repository.abstract_repository import AbstractRepository


class __RoleRepository(AbstractRepository):

    def get_model(self) -> db.Model:
        return Role

    def get_by_name(self, _name: str):
        return self.get_model().query.filter_by(name=_name).first()


roleRepository = __RoleRepository()
