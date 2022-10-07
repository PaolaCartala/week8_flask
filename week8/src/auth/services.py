from flask import request
from flask_jwt_extended import create_access_token, create_refresh_token

from src.apps.user.models import UserModel
from src.utils.responses import CommonResponses


class AuthServices:

    def login():
        data = request.get_json()

        user = UserModel.simple_filter(
            username=data['username'], password=data['password']
        )
        if user:
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return CommonResponses.ok_200(
                {'access_token': access_token, 'refresh_token': refresh_token}
            )
        else:
            return CommonResponses.unauthorized_401('Bad email or Password')
