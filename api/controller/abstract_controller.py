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

    def index(self):
        return list(map(lambda u: u.__dict__, self._get_service().get_list()))

    def get(self, id: int):
        record = self._get_service().get_by_id(id)
        if record is None:
            return self._get_response(204, None)
        else:
            return jsonify(record.__dict__)

    def store(self):
        body = self._validate_to_create(request.get_json())
        if body is not None:
            record_db = self._get_service().create(body)

            if record_db is None:
                return self._get_response(400, "Record already exists!")
            else:
                return self._get_response(201, json.dumps(record_db.__dict__))

        return self._get_response(400, "Data to create the Record is not valid!")

    def update(self, id: int):
        record = self._from_json(request.get_json())
        record_db = self._get_service().update(id, record)

        if record_db is None:
            return self._get_response(400, "Record ID does not exist!")
        else:
            return self._get_response(200, json.dumps(record_db.__dict__))

    def delete(self, id: int):
        is_deleted = self._get_service().delete(id)
        if is_deleted:
            return self._get_response(204, None)
        else:
            return self._get_response(400, "Record ID does not exist!")
