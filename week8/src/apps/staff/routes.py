from src.apps.staff.views import (
    StaffDetailAPI, StaffRetrieveAPI,
    RoleDetailAPI, RoleRetrieveAPI,
    PersonDetailAPI, PersonRetrieveAPI
)


class StaffRoutes:

    @staticmethod
    def initialize_routes(api):
        api.add_resource(StaffDetailAPI, '/staff/')
        api.add_resource(StaffRetrieveAPI, '/staff/<int:id>/')
        api.add_resource(RoleDetailAPI, '/staff/roles/')
        api.add_resource(RoleRetrieveAPI, '/staff/roles/<int:id>/')
        api.add_resource(PersonDetailAPI, '/staff/persons/')
        api.add_resource(PersonRetrieveAPI, '/staff/persons/<int:id>/')
