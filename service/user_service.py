from model.entities.user import User
from repository.user_repository import userRepository
from service.abstract_service import AbstractService


# noinspection PyMethodMayBeStatic
class __UserService(AbstractService):

    def _get_repository(self):
        return userRepository

    def get_by_username(self, username: str):
        for user in self.get_list():
            if user.username == username:
                return user
        return None

    def _contains(self, record):
        user_db = self.get_by_username(record.username)
        return False if user_db is None else True

    def _map_to_update(self, new_record: User, record_db: User):
        record_db.name = new_record.name


userService = __UserService()