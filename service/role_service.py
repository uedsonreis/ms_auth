from lib_ms_api.abstract_service import AbstractService

from model.entities.role import Role
from repository.role_repository import roleRepository


# noinspection PyMethodMayBeStatic
class __RoleService(AbstractService):

    def _get_repository(self):
        return roleRepository

    def _map_to_update(self, new_record: Role, record_db: Role):
        record_db.name = new_record.name
        record_db.description = new_record.description

    def get_by_name(self, name: str) -> Role:
        return roleRepository.get_by_name(name)

    def _contains(self, record):
        role_db = self.get_by_name(record.name)
        return False if role_db is None else True


roleService = __RoleService()
