from lib_ms_api.abstract_controller import AbstractController, authentication_required

from settings import app
from api.dto.user_dto import UserDTO
from model.entities.user import User
from service.user_service import userService


# noinspection PyMethodMayBeStatic
class UserController(AbstractController):

    def _get_service(self):
        return userService

    def _valid_to_create(self, json) -> bool:
        return "name" in json and "username" in json and "password" in json

    def _from_json(self, json):
        return User(
            json['id'] if 'id' in json else None,
            json['name'] if 'name' in json else None,
            json['username'] if 'username' in json else None,
            json['password'] if 'password' in json else None
        )

    def parser_to_dto(self, obj: User):
        return UserDTO.obj_to_dto(obj)


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
@authentication_required
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
