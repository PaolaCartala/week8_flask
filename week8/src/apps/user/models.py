from src.db import db
from src.utils.mixins import BaseModelMixin
from src.utils.queries import BaseQueries


class UserRoleModel(db.Model, BaseModelMixin, BaseQueries):

    __tablename__ = 'user_role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)

    def __repr__(self):
        return self.name


class UserModel(db.Model, BaseModelMixin, BaseQueries):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True)
    phone = db.Column(db.Integer(), nullable=True)
    address = db.Column(db.String(555), nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey("user_role.id"))
    role = db.relationship(
        "UserRoleModel", backref=db.backref("user_role", uselist=False)
    )

    def __repr__(self):
        return self.username
