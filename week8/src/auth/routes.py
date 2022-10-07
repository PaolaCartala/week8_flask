from src.auth.views import AuthAPI


class AuthRoutes:

    @staticmethod
    def initialize_routes(api):
        api.add_resource(AuthAPI, '/auth/')
