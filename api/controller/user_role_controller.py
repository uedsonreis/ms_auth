from flask import request, Response

from api.dto.role_dto import RoleDTO
from settings import app
from service.user_role_service import UserRoleService
from api.controller.abstract_controller import AbstractController


@app.route('/x')
class UserRoleController:

    @staticmethod
    @app.get('/users/<int:user_id>/roles')
    def get_roles(user_id: int):
        return list(map(lambda r: RoleDTO.obj_to_dto(r).__dict__, UserRoleService.get_roles(user_id)))

    @staticmethod
    @app.post('/users/<int:user_id>/roles')
    def add_role(user_id: int):
        role = request.get_json()

        if "id" in role:
            if UserRoleService.add_role_by_id(user_id, role['id']):
                return Response(None, 204)

        if "name" in role:
            if UserRoleService.add_role_by_name(user_id, role['name']):
                return Response(None, 204)

        return "Data to create the Record is not valid!", 400
