from datetime import timedelta
from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager

from src.db import db
from src.apps.user.routes import UserRoutes
from src.apps.user.models import UserModel, UserRoleModel
from src.apps.staff.routes import StaffRoutes
from src.apps.film.routes import FilmRoutes
from src.apps.rent.routes import RentRoutes
from src.auth.routes import AuthRoutes


class App:

    ACCESS_EXPIRES = timedelta(minutes=15)

    app = Flask(__name__)

    @classmethod
    def create_app(cls):

        api = Api(cls.app)

        # agregar en config.py
        cls.app.config['SECRET_KEY'] = 'secure-key'
        cls.app.config['JWT_SECRET_KEY'] = 'super-secret'
        cls.app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
        cls.app.config["JWT_ACCESS_TOKEN_EXPIRES"] = cls.ACCESS_EXPIRES
        cls.app.config[
            'SQLALCHEMY_DATABASE_URI'
        ] = "postgresql://postgres:123456@localhost/movierental_flask"
        cls.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        jwt = JWTManager(cls.app)

        UserRoutes.initialize_routes(api)
        StaffRoutes.initialize_routes(api)
        FilmRoutes.initialize_routes(api)
        RentRoutes.initialize_routes(api)
        AuthRoutes.initialize_routes(api)

        return cls.app

    @app.before_first_request
    def create_tables():
        db.create_all()

        #### SACAR!!! ###
        try:
            first_role = UserRoleModel(name='Admin')
            first_role.save()
            first_user = UserModel(
                first_name='Admin user',
                last_name='First user',
                username='paodev',
                password='Sas123456@',
                email='ex@ex.com',
                role_id=1
            )
            first_user.save()
        except:
            pass
