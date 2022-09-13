from lib_ms_api.abstract_dto import AbstractDTO

from model.entities.user import User


class UserDTO(AbstractDTO):

    name: str
    username: str
    password: str

    def __init__(self, id, created, modified, modifier_user, valid, name, username, password):
        self.id = id
        self.created = created
        self.modified = modified
        self.modifier_user = modifier_user
        self.valid = valid
        self.name = name
        self.username = username
        self.password = password

    def dto_to_obj(self):
        return User(
            self.id,
            self.name,
            self.username,
            self.password
        )

    @staticmethod
    def obj_to_dto(obj: User):
        dto = UserDTO(
            obj.id,
            AbstractDTO.serialize_date(obj.created),
            AbstractDTO.serialize_date(obj.modified),
            obj.modifier_user,
            obj.valid,
            obj.name,
            obj.username,
            None
        )
        del dto.password
        return dto
