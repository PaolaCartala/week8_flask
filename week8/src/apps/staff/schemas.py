from marshmallow import fields

from src.apps.staff.models import PersonModel, RoleModel, StaffModel
from src.extensions import ma


class StaffGetSchema(ma.SQLAlchemySchema):

    person = fields.Nested('PersonSchema')
    role = fields.Nested('RoleSchema')

    class Meta:
        model = StaffModel
        fields = (
            "id", "person", "role"
        )
        ordered = True


class StaffSchema(ma.SQLAlchemySchema):

    class Meta:
        model = StaffModel
        fields = (
            "id", "person_id", "role_id"
        )
        ordered = True


class RoleSchema(ma.SQLAlchemySchema):

    class Meta:
        model = RoleModel
        fields = (
            "id", "name"
        )
        ordered = True


class PersonSchema(ma.SQLAlchemySchema):

    class Meta:
        model = PersonModel
        fields = (
            "id", "name", "lastname"
        )
        ordered = True
