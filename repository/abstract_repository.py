from abc import ABC, abstractmethod
from settings import db


class AbstractRepository(ABC):

    @abstractmethod
    def get_model(self) -> db.Model:
        pass

    def find(self):
        return self.get_model().query.all()

    def get(self, id: int):
        record = self.get_model().query.get(id)
        if record is None:
            return None
        else:
            return record

    def save(self, record):
        if record.id is None:
            db.session.add(record)
            db.session.commit()
            return record

        db.session.commit()
        return record

    def delete(self, id: int):
        record = self.get(id)
        if record is None:
            return False
        else:
            db.session.delete(record)
            db.session.commit()
            return True
