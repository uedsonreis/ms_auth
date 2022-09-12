from model.entities.user import User, db
from repository.abstract_repository import AbstractRepository


class __UserRepository(AbstractRepository):

    def get_model(self) -> db.Model:
        return User


userRepository = __UserRepository()
