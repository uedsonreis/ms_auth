import jwt
from datetime import datetime

from model.entities.role import Role
from util import date_util
from model.entities.user import User
from service.user_service import userService
from service.user_role_service import UserRoleService


# noinspection PyMethodMayBeStatic
class __AuthService:
    secret = 'secretProfReisClass'

    def get_user_service(self):
        return userService

    def login(self, username: str, password: str):
        user = self.get_user_service().get_by_username(username)
        if user is not None and user.password == password and user.valid:

            roles = UserRoleService.get_roles(user.id)

            date = datetime.now()
            expires_on = datetime(date.year, date.month, date.day + 1)

            payload = {
                'sub': user.id,
                'name': user.name,
                'nickname': user.username,
                'roles': [role.name for role in roles],
                'iat': date_util.get_timestamp(date),
                'exp': date_util.get_timestamp(expires_on)
            }

            return jwt.encode(payload, key=self.secret, algorithm='HS256')
        else:
            return None

    def validate(self, token: str):
        payload = jwt.decode(token, key=self.secret, algorithms='HS256')
        user = User(payload['sub'], payload['name'], payload['nickname'], None)
        user.roles = [Role(None, role, None) for role in payload['roles']]
        return user


authService = __AuthService()
