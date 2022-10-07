from src.apps.film.views import (
    FilmDetailAPI, FilmRetrieveAPI,
    EpisodeDetailAPI, EpisodeRetrieveAPI,
    CategoryDetailAPI, CategoryRetrieveAPI,
    FilmTypeDetailAPI, FilmTypeRetrieveAPI
)


class FilmRoutes:

    @staticmethod
    def initialize_routes(api):
        api.add_resource(FilmDetailAPI, '/films/')
        api.add_resource(FilmRetrieveAPI, '/films/<int:id>/')
        api.add_resource(EpisodeDetailAPI, '/films/episodes/')
        api.add_resource(EpisodeRetrieveAPI, '/films/episodes/<int:id>/')
        api.add_resource(CategoryDetailAPI, '/films/categories/')
        api.add_resource(CategoryRetrieveAPI, '/films/categories/<int:id>/')
        api.add_resource(FilmTypeDetailAPI, '/films/filmtypes/')
        api.add_resource(FilmTypeRetrieveAPI, '/films/filmtypes/<int:id>/')
