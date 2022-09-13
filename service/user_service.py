from lib_ms_api.abstract_service import AbstractService

from model.entities.user import User
from service.role_service import roleService
from repository.user_repository import userRepository


# noinspection PyMethodMayBeStatic
class __UserService(AbstractService):

    def _get_repository(self):
        return userRepository

    def get_by_username(self, username: str) -> User:
        return userRepository.get_by_username(username)

    def _contains(self, record):
        user_db = self.get_by_username(record.username)
        return False if user_db is None else True

    def _map_to_update(self, new_record: User, record_db: User):
        record_db.name = new_record.name

    def add_role(self, id_user: int, id_rule: int):
        role_db = roleService.get_by_id(id_rule)
        userRepository.save_roles(id_user, role_db)


userService = __UserService()
