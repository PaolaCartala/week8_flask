from datetime import date

from src.apps.film.models import FilmModel


class RentUtils:

    TAX = 2

    @staticmethod
    def update_availability_substract(instance):
        film = FilmModel.get_by_id(instance.film_id)
        film.availability -= instance.quantity
        film.save()

    @staticmethod
    def update_availability_add(instance):
        film = FilmModel.get_by_id(instance.film_id)
        film.availability += instance.quantity
        film.save()

    @staticmethod
    def create_debt(obj, data):
        expected_return_day = obj.expected_return_day
        rent_date = obj.rent_date
        film_obj = FilmModel.get_by_id(obj.film_id)
        rent_days = expected_return_day - rent_date
        original_debt = rent_days.days * film_obj.price
        debt = original_debt * obj.quantity
        obj.debt = debt

    def update_tax(self, instance):
        expected_return_day = instance.expected_return_day
        if expected_return_day < date.today():
            days = date.today() - expected_return_day
            tax = days.days * self.TAX
            instance.tax = tax * instance.quantity
        instance.return_day = date.today()
        return instance.tax

    def update_debt(self, instance):
        tax = self.update_tax(instance)
        rent_date = instance.rent_date
        film_obj = FilmModel.get_by_id(instance.film_id)
        price = film_obj.price
        rent_days = date.today() - rent_date
        original_debt = ((rent_days.days + 1) * price) * instance.quantity
        debt = original_debt + tax
        instance.debt = debt
