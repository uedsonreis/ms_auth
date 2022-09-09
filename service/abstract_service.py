import json
from abc import ABC, abstractmethod


# noinspection PyMethodMayBeStatic
class AbstractService(ABC):

    @abstractmethod
    def _get_repository(self):
        pass

    def _contains(self, record):
        return False

    def get_list(self):
        return self._get_repository().find()

    def get_by_id(self, id: int):
        return self._get_repository().get(id)

    def create(self, record):
        if self._contains(record):
            return None
        else:
            record.id = None
            return self._get_repository().save(record)

    def update(self, id: int, record):
        record.id = id
        return self._get_repository().save(record)

    def delete(self, id: int):
        return self._get_repository().delete(id)
