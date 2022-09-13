from flask import request, jsonify

from settings import app
from service.auth_service import authService


@app.post('/auth/login')
def login():
    body = request.get_json()

    if "username" in body and "password" in body:
        token = authService.login(body['username'], body['password'], app.config['SECRET_KEY'], app.config['ALGORITHM'])
        if token is not None:
            return jsonify(token), 200

    return jsonify('Login/password invalid'), 401
