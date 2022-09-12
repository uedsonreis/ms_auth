from model.entities.user import User, db
from repository.abstract_repository import AbstractRepository


class __UserRepository(AbstractRepository):

    def get_model(self) -> db.Model:
        return User

    def get_by_username(self, _username: str):
        return self.get_model().query.filter_by(username=_username).first()


userRepository = __UserRepository()
