from datetime import date

from src.db import db
from src.utils.mixins import BaseModelMixin
from src.utils.queries import BaseQueries


class RentModel(db.Model, BaseModelMixin, BaseQueries):

    __tablename__ = 'rent'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship(
        'UserModel', backref=db.backref("user_rent", uselist=False)
    )
    film_id = db.Column(db.Integer, db.ForeignKey("film.id"))
    film = db.relationship(
        "FilmModel", backref=db.backref("film_rent", uselist=False)
    )
    quantity = db.Column(db.Integer(), nullable=False, default=1)
    rent_date = db.Column(db.Date(), nullable=False, default=date.today)
    expected_return_day = db.Column(db.Date(), nullable=False)
    return_day = db.Column(db.Date(), nullable=True)
    tax = db.Column(db.Integer(), nullable=True, default=0)
    debt = db.Column(db.Integer(), nullable=True, default=0)

    def __repr__(self):
        return f'{self.rent_date} - {self.film}'
