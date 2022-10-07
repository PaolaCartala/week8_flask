from flask_jwt_extended import jwt_required
from flask_restx import Resource

from src.apps.user.schemas import UserSchema, UserGetSchema, UserRoleSchema
from src.apps.user.models import UserModel, UserRoleModel
from src.utils.services import CommonServices
from src.auth.decorators import AuthDecorators


class UserDetailAPI(Resource):

    schema_class = UserSchema()
    model_class = UserModel
    services_class = CommonServices

    @classmethod
    @jwt_required()
    def get(cls):
        return cls.services_class.list(UserGetSchema(), cls.model_class)

    @classmethod
    @AuthDecorators.check_role(['Admin'])
    def post(cls):
        return cls.services_class.create(cls.schema_class, cls.model_class)


class UserRetrieveAPI(Resource):

    schema_class = UserSchema()
    model_class = UserModel
    services_class = CommonServices

    @classmethod
    @jwt_required()
    def put(cls, id):
        return cls.services_class.update(id, cls.schema_class, cls.model_class)

    @classmethod
    @jwt_required()
    def delete(cls, id):
        return cls.services_class.destroy(id, cls.model_class)


class UserRoleDetailAPI(Resource):

    schema_class = UserRoleSchema()
    model_class = UserRoleModel
    services_class = CommonServices

    @classmethod
    @jwt_required()
    def get(cls):
        return cls.services_class.list(cls.schema_class, cls.model_class)

    @classmethod
    @AuthDecorators.check_role(['Admin'])
    def post(cls):
        return cls.services_class.create(cls.schema_class, cls.model_class)


class UserRoleRetrieveAPI(Resource):

    schema_class = UserRoleSchema()
    model_class = UserRoleModel
    services_class = CommonServices

    @classmethod
    @jwt_required()
    def put(cls, id):
        return cls.services_class.update(id, cls.schema_class, cls.model_class)

    @classmethod
    @jwt_required()
    def delete(cls, id):
        return cls.services_class.destroy(id, cls.model_class)
