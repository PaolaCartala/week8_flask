from marshmallow import fields, validate

from src.extensions import ma
from src.utils.validators import CommonValidators
from src.apps.rent.models import RentModel


class RentGetSchema(ma.SQLAlchemySchema):

    user = fields.Nested('UserGetSchema')
    film = fields.Nested('FilmGetSchema')

    class Meta:
        model = RentModel
        fields = (
            'id', 'user', 'film', 'quantity', 'rent_date',
            'expected_return_day', 'return_day', 'tax', 'debt', 'updated_by'
        )
        ordered = True


class RentSchema(ma.SQLAlchemySchema):

    quantity = fields.Integer(
        validate=[validate.Range(min=1)],
        required=True
    )
    rent_date = fields.Date(
        validate=[CommonValidators.validator_today],
        required=True
    )
    expected_return_day = fields.Date(
        validate=[CommonValidators.validate_date,
                  CommonValidators.validator_max_days],
        required=True
    )
    return_day = fields.Date(
        validate=[CommonValidators.validate_date,
                  CommonValidators.validator_today],
        allow_none=True
    )
    tax = fields.Integer(
        validate=[validate.Range(min=0)]
    )
    debt = fields.Integer(
        validate=[validate.Range(min=0)]
    )

    class Meta:
        model = RentModel
        fields = (
            'id', 'user_id', 'film_id', 'quantity', 'rent_date',
            'expected_return_day', 'return_day', 'tax', 'debt', 'updated_by'
        )
        ordered = True
