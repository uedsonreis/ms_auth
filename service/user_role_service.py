from model.entities.role import Role, db
from model.entities.user import User
from repository.role_repository import roleRepository
from repository.user_repository import userRepository


class UserRoleService:

    @staticmethod
    def get_roles(user_id: int):
        user: User = userRepository.get(user_id)
        return user.roles

    @staticmethod
    def add_role_by_id(user_id: int, role_id: int) -> bool:
        role: Role = roleRepository.get(role_id)
        return UserRoleService.add_role(user_id, role)

    @staticmethod
    def add_role_by_name(user_id: int, role_name: str) -> bool:
        role: Role = None
        roles = roleRepository.find()

        for role_db in roles:
            if role_db.name == role_name:
                role = role_db

        return UserRoleService.add_role(user_id, role)

    @staticmethod
    def add_role(user_id: int, role: Role) -> bool:
        if role is None:
            return False

        user: User = userRepository.get(user_id)

        if user is None:
            return False

        user.roles.insert(len(user.roles), role)
        db.session.commit()
        return True
