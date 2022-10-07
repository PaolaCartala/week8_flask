from datetime import date, timedelta
from marshmallow.exceptions import ValidationError


class CommonValidators:

    @staticmethod
    def validate_date(value):
        if value < date.today():
            raise ValidationError(
                "Please enter a valid date!"
            )

    @staticmethod
    def validator_max_days(value):
        if value > date.today() + timedelta(days=15):
            raise ValidationError(
                "You can't rent the film for more than 15 days"
            )

    @staticmethod
    def validator_today(value):
        if value > date.today():
            raise ValidationError(
                "The date can't be greater than today!"
            )

    # from serializer
    def validate(self, data):
        stock = data['stock']
        availability = data['availability']
        if availability > stock:
            raise ValidationError(
                "The availability can't be higher than stock"
            )
        return data
