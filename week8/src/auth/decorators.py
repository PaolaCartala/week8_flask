from flask import request
from functools import wraps
from flask_jwt_extended import jwt_required

from src.apps.user.models import UserModel, UserRoleModel
from src.utils.responses import CommonResponses


class AuthDecorators:

    # ROLE = 'Admin'

    def check_role(roles):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                for r in roles:
                    is_role = UserRoleModel.simple_filter(
                        name=r
                    )
                    if is_role is not None:
                        # verifica si el user tiene el rol
                        is_user = request.user.role_id == is_role.id
                        if is_user is not None:
                            return func(*args, **kwargs)
                CommonResponses.bad_request_400()
                # abort(403)  # CommonResponses
            return wrapper
        return decorator

    """def admin_required(function):
        @wraps(function)
        def decorated_function(*args, **kws):

            is_admin = getattr(current_user, 'is_admin', False)
            if not is_admin:
                abort(401)
            return function(*args, **kws)
        return decorated_function"""
