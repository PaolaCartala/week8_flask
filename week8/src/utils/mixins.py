from src.db import db


class BaseModelMixin:

    def commit(self):
        db.session.commit()

    def save(self):
        db.session.add(self)
        self.commit()

    def delete(self):
        db.session.delete(self)
        self.commit()
