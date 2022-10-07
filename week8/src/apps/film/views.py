from flask_restx import Resource
from flask_jwt_extended import jwt_required

from src.apps.film.schemas import (
    FilmGetSchema, FilmSchema,
    EpisodeGetSchema, EpisodeSchema,
    CategorySchema, FilmTypeSchema
)
from src.apps.film.models import (
    CategoryModel, FilmTypeModel,
    FilmModel, EpisodeModel
)
from src.utils.services import CommonServices
from src.apps.film.services import FilmServices


class FilmDetailAPI(Resource):

    schema_class = FilmSchema()
    model_class = FilmModel
    services_class = CommonServices

    @classmethod
    def get(cls):
        return cls.services_class.list(FilmGetSchema(), cls.model_class)

    @classmethod
    @jwt_required()
    def post(cls):
        return FilmServices.create(cls.schema_class, cls.model_class)


class FilmRetrieveAPI(Resource):

    schema_class = FilmSchema()
    model_class = FilmModel
    services_class = CommonServices

    @classmethod
    @jwt_required()
    def put(cls, id):
        return FilmServices.update(id, cls.schema_class, cls.model_class)

    @classmethod
    @jwt_required()
    def delete(cls, id):
        return cls.services_class.destroy(id, cls.model_class)


class EpisodeDetailAPI(Resource):

    schema_class = EpisodeSchema()
    model_class = EpisodeModel
    services_class = CommonServices

    @classmethod
    def get(cls):
        return cls.services_class.list(EpisodeGetSchema(), cls.model_class)

    @classmethod
    @jwt_required()
    def post(cls):
        return cls.services_class.create(cls.schema_class, cls.model_class)


class EpisodeRetrieveAPI(Resource):

    schema_class = EpisodeSchema()
    model_class = EpisodeModel
    services_class = CommonServices

    @classmethod
    @jwt_required()
    def put(cls, id):
        return cls.services_class.update(id, cls.schema_class, cls.model_class)

    @classmethod
    @jwt_required()
    def delete(cls, id):
        return cls.services_class.destroy(id, cls.model_class)


class CategoryDetailAPI(Resource):

    schema_class = CategorySchema()
    model_class = CategoryModel
    services_class = CommonServices

    @classmethod
    @jwt_required()
    def get(cls):
        return cls.services_class.list(cls.schema_class, cls.model_class)

    @classmethod
    @jwt_required()
    def post(cls):
        return cls.services_class.create(cls.schema_class, cls.model_class)


class CategoryRetrieveAPI(Resource):

    schema_class = CategorySchema()
    model_class = CategoryModel
    services_class = CommonServices

    @classmethod
    @jwt_required()
    def put(cls, id):
        return cls.services_class.update(id, cls.schema_class, cls.model_class)

    @classmethod
    @jwt_required()
    def delete(cls, id):
        return cls.services_class.destroy(id, cls.model_class)


class FilmTypeDetailAPI(Resource):

    schema_class = FilmTypeSchema()
    model_class = FilmTypeModel
    services_class = CommonServices

    @classmethod
    @jwt_required()
    def get(cls):
        return cls.services_class.list(cls.schema_class, cls.model_class)

    @classmethod
    @jwt_required()
    def post(cls):
        return cls.services_class.create(cls.schema_class, cls.model_class)


class FilmTypeRetrieveAPI(Resource):

    schema_class = FilmTypeSchema()
    model_class = FilmTypeModel
    services_class = CommonServices

    @classmethod
    @jwt_required()
    def put(cls, id):
        return cls.services_class.update(id, cls.schema_class, cls.model_class)

    @classmethod
    @jwt_required()
    def delete(cls, id):
        return cls.services_class.destroy(id, cls.model_class)
