from marshmallow import fields, validate, validates_schema
from marshmallow.exceptions import ValidationError

from src.extensions import ma
from src.apps.film.models import (
    FilmModel, CategoryModel, FilmTypeModel, EpisodeModel
)
from src.utils.validators import CommonValidators


class FilmGetSchema(ma.SQLAlchemySchema):

    film_type = fields.Nested('FilmTypeSchema')
    categories = fields.Nested('CategorySchema', many=True)
    staff = fields.Nested('StaffGetSchema', many=True)

    class Meta:
        model = FilmModel
        fields = (
            'id', 'title', 'description', 'image',
            'stock', 'price', 'availability', 'release_date',
            'film_type', 'categories', 'staff'
        )
        ordered = True


class FilmSchema(ma.SQLAlchemySchema):

    stock = fields.Integer(
        validate=[validate.Range(min=1)],
        required=True
    )
    price = fields.Float(
        validate=[validate.Range(min=0.00)],
        required=True
    )
    availability = fields.Integer(
        validate=[validate.Range(min=1)],
        required=True
    )
    release_date = fields.Date(
        validate=[CommonValidators.validator_today],
        required=True
    )

    class Meta:
        model = FilmModel
        fields = (
            'id', 'title', 'description', 'image',
            'stock', 'price', 'availability', 'release_date',
            'film_type_id', 'categories', 'staff'
        )
        ordered = True

    @validates_schema
    def validate(self, data, **kwargs):
        stock = data['stock']
        availability = data['availability']
        if availability > stock:
            raise ValidationError(
                "The availability can't be higher than stock"
            )
        return data


class EpisodeGetSchema(ma.SQLAlchemySchema):

    season = fields.Nested('FilmGetSchema')

    class Meta:
        model = EpisodeModel
        fields = (
            'id', 'season', 'number', 'title',
            'description', 'release_date'
        )
        ordered = True


class EpisodeSchema(ma.SQLAlchemySchema):

    number = fields.Integer(
        validate=[validate.Range(min=1)],
        required=True
    )
    release_date = fields.Date(
        validate=[CommonValidators.validator_today],
        required=True
    )

    class Meta:
        model = EpisodeModel
        fields = (
            'id', 'season_id', 'number', 'title',
            'description', 'release_date'
        )
        ordered = True


class CategorySchema(ma.SQLAlchemySchema):

    class Meta:
        model = CategoryModel
        fields = (
            'id', 'name'
        )
        ordered = True


# FilmTypeModel
class FilmTypeSchema(ma.SQLAlchemySchema):

    class Meta:
        model = FilmTypeModel
        fields = (
            'id', 'name'
        )
        include_fk = True
