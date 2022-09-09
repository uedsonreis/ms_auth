from model.entities.user import User
from repository.abstract_repository import AbstractRepository


class __UserRepository(AbstractRepository):

    def get_query(self):
        return User.query


userRepository = __UserRepository()
