from src.db import db
from src.utils.mixins import BaseModelMixin
from src.utils.queries import BaseQueries


class PersonModel(db.Model, BaseModelMixin, BaseQueries):

    __tablename__ = 'staff_person'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'{self.lastname}, {self.name}'


class RoleModel(db.Model, BaseModelMixin, BaseQueries):

    __tablename__ = 'staff_role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)

    def __repr__(self):
        return self.name


class StaffModel(db.Model, BaseModelMixin, BaseQueries):

    __tablename__ = 'staff'

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("staff_person.id"))
    person = db.relationship(
        "PersonModel", backref=db.backref("staff_person", uselist=False)
    )
    role_id = db.Column(db.Integer, db.ForeignKey("staff_role.id"))
    role = db.relationship(
        "RoleModel", backref=db.backref("staff_role", uselist=False)
    )

    def __repr__(self):
        return f'{self.role_id} - {self.person_id}'
