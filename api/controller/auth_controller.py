from flask import request, Response

from settings import app
from service.auth_service import authService


def _get_response(http_code: int, message):
    return Response(message, http_code, mimetype="application/json")


def _validate_to_login(user):
    return "username" in user and "password" in user


class AuthController:

    __service = authService

    def login(self):
        body = request.get_json()

        if _validate_to_login(body):
            token = self.__service.login(body['username'], body['password'])
            if token is not None:
                return token

        return _get_response(401, "Login/password invalid")


controller = AuthController()


@app.post('/auth/login')
def login():
    return controller.login()
