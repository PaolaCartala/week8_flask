from src.apps.rent.views import (
    RentDetailAPI, RentRetrieveAPI
)


class RentRoutes:

    @staticmethod
    def initialize_routes(api):
        api.add_resource(RentDetailAPI, '/rents/')
        api.add_resource(RentRetrieveAPI, '/rents/<int:id>/')
