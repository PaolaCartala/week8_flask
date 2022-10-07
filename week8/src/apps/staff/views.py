from flask_jwt_extended import jwt_required
from flask_restx import Resource

from src.apps.staff.models import StaffModel, RoleModel, PersonModel
from src.apps.staff.schemas import (
    StaffGetSchema, StaffSchema, RoleSchema, PersonSchema
)
from src.utils.services import CommonServices


class StaffDetailAPI(Resource):

    schema_class = StaffSchema()
    model_class = StaffModel
    services_class = CommonServices

    @classmethod
    @jwt_required()
    def get(cls):
        return cls.services_class.list(StaffGetSchema(), cls.model_class)

    @classmethod
    @jwt_required()
    def post(cls):
        return cls.services_class.create(cls.schema_class, cls.model_class)


class StaffRetrieveAPI(Resource):

    schema_class = StaffSchema()
    model_class = StaffModel
    services_class = CommonServices

    @classmethod
    @jwt_required()
    def put(cls, id):
        return cls.services_class.update(id, cls.schema_class, cls.model_class)

    @classmethod
    @jwt_required()
    def delete(cls, id):
        return cls.services_class.destroy(id, cls.model_class)


class RoleDetailAPI(Resource):

    schema_class = RoleSchema()
    model_class = RoleModel
    services_class = CommonServices

    @classmethod
    @jwt_required()
    def get(cls):
        return cls.services_class.list(cls.schema_class, cls.model_class)

    @classmethod
    @jwt_required()
    def post(cls):
        return cls.services_class.create(cls.schema_class, cls.model_class)


class RoleRetrieveAPI(Resource):

    schema_class = RoleSchema()
    model_class = RoleModel
    services_class = CommonServices

    @classmethod
    @jwt_required()
    def put(cls, id):
        return cls.services_class.update(id, cls.schema_class, cls.model_class)

    @classmethod
    @jwt_required()
    def delete(cls, id):
        return cls.services_class.destroy(id, cls.model_class)


class PersonDetailAPI(Resource):

    schema_class = PersonSchema()
    model_class = PersonModel
    services_class = CommonServices

    @classmethod
    @jwt_required()
    def get(cls):
        return cls.services_class.list(cls.schema_class, cls.model_class)

    @classmethod
    @jwt_required()
    def post(cls):
        return cls.services_class.create(cls.schema_class, cls.model_class)


class PersonRetrieveAPI(Resource):

    schema_class = PersonSchema()
    model_class = PersonModel
    services_class = CommonServices

    @classmethod
    @jwt_required()
    def put(cls, id):
        return cls.services_class.update(id, cls.schema_class, cls.model_class)

    @classmethod
    @jwt_required()
    def delete(cls, id):
        return cls.services_class.destroy(id, cls.model_class)
