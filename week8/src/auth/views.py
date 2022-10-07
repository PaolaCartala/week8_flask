from flask_restx import Resource

from src.auth.services import AuthServices


class AuthAPI(Resource):

    @classmethod
    def post(cls):
        return AuthServices.login()
