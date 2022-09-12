from functools import wraps

from flask import request, Response, jsonify

from settings import app
from service.auth_service import authService
from api.controller.abstract_controller import AbstractController


def authentication_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            authorization = request.headers['authorization']
            token = authorization.split(' ')[1]
            user = authService.validate(token)
            request.logged = user
        except:
            return jsonify('Need a valid token to access this resource'), 401
        return f(*args, **kwargs)

    return wrapper


@app.post('/auth/login')
def login():
    body = request.get_json()

    if "username" in body and "password" in body:
        token = authService.login(body['username'], body['password'])
        if token is not None:
            return jsonify(token), 200

    return jsonify('Login/password invalid'), 401
