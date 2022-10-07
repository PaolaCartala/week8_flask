from marshmallow import fields, validate

from src.apps.user.models import UserModel, UserRoleModel
from src.extensions import ma


class UserGetSchema(ma.SQLAlchemySchema):

    role = fields.Nested('UserRoleSchema')

    class Meta:
        model = UserModel
        fields = (
            "id", "first_name", "last_name", "username", "email",
            "phone", "address", "role"
        )
        ordered = True


class UserSchema(ma.SQLAlchemySchema):

    username = fields.Str(
        validate=[validate.Length(min=6, max=255)], required=True,
        unique=True
    )
    password = fields.Str(
        validate=[validate.Length(min=8, max=255),
                  validate.Regexp('^(?=.*[0-9])'+'(?=.*[a-z])(?=.*[A-Z])'+'(?=.*[@#$%^&+=])')],  # noqa:E501
        required=True
    )
    email = fields.Email(required=True, unique=True)

    class Meta:
        model = UserModel
        fields = (
            "id", "first_name", "last_name", "username", "password", "email",
            "phone", "address", "role_id"
        )
        ordered = True


class UserRoleSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = UserRoleModel
        include_fk = True
        ordered = True
