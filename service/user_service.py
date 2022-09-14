import bcrypt
from flask import abort, Response
from lib_ms_api.abstract_service import AbstractService

from model.entities.user import User
from service.role_service import roleService
from repository.user_repository import userRepository

SALT = 10
UTF8 = 'utf-8'


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
        if new_record.modifier_user == record_db.username:
            record_db.name = new_record.name
        else:
            abort(Response("Permission denied", 403))

    def create(self, record: User):
        if self._contains(record):
            return None
        else:
            record.id = None
            record.password = record.password.encode(UTF8)
            record.password = bcrypt.hashpw(record.password, bcrypt.gensalt(SALT))
            record.password = record.password.decode(UTF8)
            return self._get_repository().save(record)

    def login(self, username: str, password: str):
        user = self.get_by_username(username)

        if user is not None and user.valid:
            check = password.encode(UTF8)
            hashed = user.password.encode(UTF8)

            if bcrypt.checkpw(check, hashed):
                return user

        return None

    def add_role(self, id_user: int, id_rule: int):
        role_db = roleService.get_by_id(id_rule)
        userRepository.save_roles(id_user, role_db)


userService = __UserService()
