from api.controller.auth_controller import authentication_required
from api.dto.role_dto import RoleDTO
from settings import app
from model.entities.role import Role
from service.role_service import roleService
from api.controller.abstract_controller import AbstractController


# noinspection PyMethodMayBeStatic
class RoleController(AbstractController):

    def _get_service(self):
        return roleService

    def _valid_to_create(self, json) -> bool:
        return "name" in json

    def _from_json(self, json):
        return Role(
            json['id'] if 'id' in json else None,
            json['name'] if 'name' in json else None,
            json['description'] if 'description' in json else None
        )

    def parser_to_dto(self, obj: Role):
        return RoleDTO.obj_to_dto(obj)


PATH = '/roles'
controller = RoleController()


@app.get(PATH)
@authentication_required
def index_roles():
    return controller.index()


@app.get(PATH+'/<int:id>')
@authentication_required
def get_role(id: int):
    return controller.get(id)


@app.post(PATH)
@authentication_required
def store_role():
    return controller.store()


@app.put(PATH+'/<int:id>')
@authentication_required
def update_role(id: int):
    return controller.update(id)


@app.delete(PATH+'/<int:id>')
@authentication_required
def delete_role(id: int):
    return controller.delete(id)
