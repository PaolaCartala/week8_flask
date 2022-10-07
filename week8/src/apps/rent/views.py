from flask_jwt_extended import jwt_required
from flask_restx import Resource

from src.apps.rent.schemas import RentGetSchema, RentSchema
from src.apps.rent.models import RentModel
from src.utils.services import CommonServices
from src.apps.rent.services import RentServices


class RentDetailAPI(Resource):

    schema_class = RentSchema()
    model_class = RentModel
    services_class = CommonServices

    @classmethod
    @jwt_required()
    def get(cls):
        return cls.services_class.list(RentGetSchema(), cls.model_class)

    @classmethod
    @jwt_required()
    def post(cls):
        return RentServices.create(cls.schema_class, cls.model_class)


class RentRetrieveAPI(Resource):

    schema_class = RentSchema()
    model_class = RentModel
    services_class = CommonServices

    @classmethod
    @jwt_required()
    def put(cls, id):
        return RentServices.update(id, cls.schema_class, cls.model_class)

    @classmethod
    @jwt_required()
    def delete(cls, id):
        return cls.services_class.destroy(id, cls.model_class)
