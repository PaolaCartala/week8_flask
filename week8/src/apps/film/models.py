from src.db import db
from src.utils.mixins import BaseModelMixin
from src.utils.queries import BaseQueries


class CategoryModel(db.Model, BaseModelMixin, BaseQueries):

    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)

    def __repr__(self):
        return self.name


class FilmTypeModel(db.Model, BaseModelMixin, BaseQueries):

    __tablename__ = 'filmtype'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)

    def __repr__(self):
        return self.name


class FilmCategories(db.Model, BaseModelMixin, BaseQueries):

    __tablename__ = 'film_category'

    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'))  # left
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))  # right


class FilmStaff(db.Model, BaseModelMixin, BaseQueries):

    __tablename__ = 'film_staff'

    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'))  # left
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'))  # right


class FilmModel(db.Model, BaseModelMixin, BaseQueries):

    __tablename__ = 'film'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.String(999), nullable=True)
    image = db.Column(db.String(255), nullable=True)
    stock = db.Column(db.Integer(), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    availability = db.Column(db.Integer(), nullable=False)
    release_date = db.Column(db.Date(), nullable=False)
    film_type_id = db.Column(db.Integer, db.ForeignKey("filmtype.id"))
    film_type = db.relationship(
        "FilmTypeModel", backref=db.backref("filmtype", uselist=False)
    )
    categories = db.relationship(
        'CategoryModel', secondary='film_category',
        foreign_keys=[FilmCategories.film_id, FilmCategories.category_id],
        backref='categories'
    )
    staff = db.relationship(
        "StaffModel", secondary='film_staff',
        foreign_keys=[FilmStaff.film_id, FilmStaff.staff_id],
        backref='staff'
    )

    def __repr__(self):
        return self.title


class EpisodeModel(db.Model, BaseModelMixin, BaseQueries):

    __tablename__ = 'episode'

    id = db.Column(db.Integer, primary_key=True)
    season_id = db.Column(db.Integer, db.ForeignKey("film.id"))
    season = db.relationship(
        "FilmModel", backref=db.backref("film", uselist=False)
    )
    number = db.Column(db.Integer(), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(555), nullable=True)
    release_date = db.Column(db.Date(), nullable=False)

    def __repr__(self):
        return f'{self.number} - {self.title}'
