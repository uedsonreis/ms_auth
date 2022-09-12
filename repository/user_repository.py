from model.entities.user import User, db
from repository.abstract_repository import AbstractRepository


class __UserRepository(AbstractRepository):

    def get_model(self) -> db.Model:
        return User

    def get_roles(self, id: int):
        pass

    def save_roles(self, id: int, role):
        user: User = self.get(id)

        user.roles.insert(len(user.roles), role)
        db.session.commit()


userRepository = __UserRepository()
