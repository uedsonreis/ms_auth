from service.user_service import userService
from datetime import datetime
import jwt

from util import date_util


# noinspection PyMethodMayBeStatic
class __AuthService:

    secret = 'secretProfReisClass'

    def get_user_service(self):
        return userService

    def login(self, username: str, password: str):
        user = self.get_user_service().get_by_username(username)
        if user.password == password and user.valid:

            date = datetime.now()
            expires_on = datetime(date.year, date.month, date.day + 1)

            roles = []

            if user.admin:
                roles.insert(0, 'admin')

            payload = {
                'sub': user.id,
                'name': user.name,
                'nickname': user.username,
                'roles': roles,
                'iat': date_util.get_timestamp(date),
                'exp': date_util.get_timestamp(expires_on)
            }

            return jwt.encode(payload, key=self.secret, algorithm='HS256')
        else:
            return None


authService = __AuthService()
