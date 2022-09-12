from model.entities.role import Role, db
from repository.abstract_repository import AbstractRepository


class __RoleRepository(AbstractRepository):

    def get_model(self) -> db.Model:
        return Role


roleRepository = __RoleRepository()
