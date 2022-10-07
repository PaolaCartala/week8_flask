from src.apps.user.views import (
    UserDetailAPI, UserRetrieveAPI,
    UserRoleDetailAPI, UserRoleRetrieveAPI
)


class UserRoutes:

    @staticmethod
    def initialize_routes(api):
        api.add_resource(UserDetailAPI, '/users/')
        api.add_resource(UserRetrieveAPI, '/users/<int:id>/')
        api.add_resource(UserRoleDetailAPI, '/users/roles/')
        api.add_resource(UserRoleRetrieveAPI, '/users/roles/<int:id>/')
