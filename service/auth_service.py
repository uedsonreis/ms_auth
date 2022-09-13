from datetime import datetime

import bcrypt
from lib_ms_api.abstract_service import generate_jwt_token

from util import date_util
from model.entities.role import Role
from model.entities.user import User
from service.user_service import userService
from service.user_role_service import UserRoleService


# noinspection PyMethodMayBeStatic
class __AuthService:

    def get_user_service(self):
        return userService

    def login(self, username: str, password: str, secret: str, algorithm: str):
        user = self.get_user_service().login(username, password)
        if user is not None:
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

            return {'token': generate_jwt_token(payload, secret, algorithm)}
        else:
            return None

    def parser_payload(self, payload):
        user = User(payload['sub'], payload['name'], payload['nickname'], None)
        user.roles = [Role(None, role, None) for role in payload['roles']]
        return user


authService = __AuthService()
