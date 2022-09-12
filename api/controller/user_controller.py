from settings import app
from model.entities.user import User
from service.user_service import userService
from api.controller.abstract_controller import AbstractController


# noinspection PyMethodMayBeStatic
class UserController(AbstractController):

    def _get_service(self):
        return userService

    def _validate_to_create(self, json):
        if "name" in json and "username" in json and "password" in json:
            return User(None, json['name'], json['username'], json['password'])
        else:
            return None

    def _from_json(self, json):
        return User(
            json['id'] if 'id' in json else None,
            json['name'] if 'name' in json else None,
            json['username'] if 'username' in json else None,
            json['password'] if 'password' in json else None
        )


PATH = '/users'
controller = UserController()


@app.get(PATH)
def index():
    return controller.index()


@app.get(PATH+'/<int:id>')
def get(id: int):
    return controller.get(id)


@app.post(PATH)
def store():
    return controller.store()


@app.put(PATH+'/<int:id>')
def update(id: int):
    return controller.update(id)


@app.delete(PATH+'/<int:id>')
def delete(id: int):
    return controller.delete(id)
