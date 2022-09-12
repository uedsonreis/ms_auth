import json
from abc import ABC, abstractmethod
from flask import jsonify, request, Response


# noinspection PyMethodMayBeStatic
from api.dto.abstract_dto import AbstractDTO
from service.abstract_service import AbstractService


# noinspection PyMethodMayBeStatic
class AbstractController(ABC):

    @abstractmethod
    def _get_service(self) -> AbstractService:
        pass

    @abstractmethod
    def _from_json(self, json):
        pass

    @abstractmethod
    def _valid_to_create(self, json) -> bool:
        pass

    @abstractmethod
    def parser_to_dto(self, obj) -> AbstractDTO:
        pass

    @staticmethod
    def get_response(http_code: int, message: str):
        return Response(message, http_code, mimetype="application/json")

    def serialize_list(self, list):
        return [self.parser_to_dto(e).__dict__ for e in list]

    def index(self):
        list = self.serialize_list(self._get_service().get_list())
        return AbstractController.get_response(200, json.dumps(list))

    def get(self, id: int):
        record = self._get_service().get_by_id(id)
        if record is None:
            return AbstractController.get_response(204, None)
        else:
            dto = self.parser_to_dto(record)
            return AbstractController.get_response(200, json.dumps(dto.__dict__))

    def store(self):
        body = request.get_json()

        if self._valid_to_create(body):
            record = self._from_json(body)
            record.modifier_user = request.logged.username

            if record is not None:
                record_db = self._get_service().create(record)

                if record_db is None:
                    return AbstractController.get_response(400, "Record already exists!")
                else:
                    dto = self.parser_to_dto(record_db)
                    return AbstractController.get_response(201, json.dumps(dto.__dict__))

        return AbstractController.get_response(400, "Data to create the Record is not valid!")

    def update(self, id: int):
        record = self._from_json(request.get_json())
        record.modifier_user = request.logged.username
        record_db = self._get_service().update(id, record)

        if record_db is None:
            return AbstractController.get_response(400, "Record ID does not exist!")
        else:
            dto = self.parser_to_dto(record_db)
            return AbstractController.get_response(200, json.dumps(dto.__dict__))

    def delete(self, id: int):
        is_deleted = self._get_service().delete(id)
        if is_deleted:
            return AbstractController.get_response(204, None)
        else:
            return AbstractController.get_response(400, "Record ID does not exist!")
