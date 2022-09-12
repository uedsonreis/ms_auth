from api.dto.abstract_dto import AbstractDTO
from model.entities.role import Role


class RoleDTO(AbstractDTO):

    name: str
    description: str

    def __init__(self, id, created, modified, modifier_user, valid, name, description):
        self.id = id
        self.created = created
        self.modified = modified
        self.modifier_user = modifier_user
        self.valid = valid
        self.name = name
        self.description = description

    def dto_to_obj(self):
        return Role(
            self.id,
            self.name,
            self.description
        )

    @staticmethod
    def obj_to_dto(obj: Role):
        return RoleDTO(
            obj.id,
            AbstractDTO.serialize_date(obj.created),
            AbstractDTO.serialize_date(obj.modified),
            obj.modifier_user,
            obj.valid,
            obj.name,
            obj.description
        )
