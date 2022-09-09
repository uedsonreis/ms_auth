import json
from abc import ABC, abstractmethod
from flask import jsonify, request, Response


# noinspection PyMethodMayBeStatic
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
    def _validate_to_create(self, json):
        pass

    def _get_response(self, http_code: int, message):
        return Response(message, http_code, mimetype="application/json")

    def serialize_list(self, list):
        return [e.serialize() for e in list]

    def index(self):
        return self.serialize_list(self._get_service().get_list())
        # return list(map(lambda u: u.__dict__, self._get_service().get_list()))

    def get(self, id: int):
        record = self._get_service().get_by_id(id)
        if record is None:
            return self._get_response(204, None)
        else:
            return jsonify(record.serialize())

    def store(self):
        body = self._validate_to_create(request.get_json())
        if body is not None:
            record_db = self._get_service().create(body)

            if record_db is None:
                return self._get_response(400, "Record already exists!")
            else:
                res = jsonify(record_db.serialize())
                res.status_code = 201
                return res

        return self._get_response(400, "Data to create the Record is not valid!")

    def update(self, id: int):
        record = self._from_json(request.get_json())
        record_db = self._get_service().update(id, record)

        if record_db is None:
            return self._get_response(400, "Record ID does not exist!")
        else:
            return jsonify(record_db.serialize())

    def delete(self, id: int):
        is_deleted = self._get_service().delete(id)
        if is_deleted:
            return self._get_response(204, None)
        else:
            return self._get_response(400, "Record ID does not exist!")
