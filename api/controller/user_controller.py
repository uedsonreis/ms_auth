from flask import Response, request
from lib_ms_api.abstract_controller import AbstractController, authentication_required

from settings import app
from api.dto.user_dto import UserDTO
from model.entities.user import User
from service.user_service import userService


# noinspection PyMethodMayBeStatic
class UserController(AbstractController):

    def _get_service(self):
        return userService

    def _valid_to_create(self, json) -> str:
        if "name" not in json:
            return "NAME is required"
        if "username" not in json:
            return "USERNAME is required"
        if "password" not in json:
            return "PASSWORD is required"
        return None

    def _from_json(self, json):
        return User(
            json['id'] if 'id' in json else None,
            json['name'] if 'name' in json else None,
            json['username'] if 'username' in json else None,
            json['password'] if 'password' in json else None
        )

    def parser_to_dto(self, obj: User):
        return UserDTO.obj_to_dto(obj)

    def delete(self, id: int):
        logged: User = self._get_service().get_by_id(request.logged['sub'])
        if logged is not None and (logged.admin or logged.id == id):

            is_deleted = self._get_service().delete(id)
            if is_deleted:
                return Response(None, 204)
            else:
                return "Record ID does not exist!", 400

        return "Permission denied", 403


PATH = '/users'
controller = UserController()


@app.get(PATH)
@authentication_required
def index_users():
    return controller.index()


@app.get(PATH+'/<int:id>')
@authentication_required
def get_user(id: int):
    return controller.get(id)


@app.post(PATH)
def store_user():
    return controller.store()


@app.put(PATH+'/<int:id>')
@authentication_required
def update_user(id: int):
    return controller.update(id)


@app.delete(PATH+'/<int:id>')
@authentication_required
def delete_user(id: int):
    return controller.delete(id)
