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

    def serialize_list(self, list):
        return [self.parser_to_dto(e).__dict__ for e in list]

    def index(self):
        list = self.serialize_list(self._get_service().get_list())
        return jsonify(list), 200

    def get(self, id: int):
        record = self._get_service().get_by_id(id)
        if record is None:
            return Response(None, 204)
        else:
            dto = self.parser_to_dto(record)
            return jsonify(dto.__dict__), 200

    def store(self):
        body = request.get_json()

        if self._valid_to_create(body):
            record = self._from_json(body)
            record.modifier_user = request.logged.username

            if record is not None:
                record_db = self._get_service().create(record)

                if record_db is None:
                    return Response("Record already exists!", 400)
                else:
                    dto = self.parser_to_dto(record_db)
                    return jsonify(dto.__dict__), 201

        return "Data to create the Record is not valid!", 400

    def update(self, id: int):
        record = self._from_json(request.get_json())
        record.modifier_user = request.logged.username
        record_db = self._get_service().update(id, record)

        if record_db is None:
            return "Record ID does not exist", 400
        else:
            dto = self.parser_to_dto(record_db)
            return jsonify(dto.__dict__)

    def delete(self, id: int):
        is_deleted = self._get_service().delete(id)
        if is_deleted:
            return Response(None, 204)
        else:
            return "Record ID does not exist!", 400
