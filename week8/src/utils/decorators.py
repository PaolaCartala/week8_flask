from sqlalchemy.exc import IntegrityError

from src.utils.responses import CommonResponses


class ExceptionsDecorator:

    def integrity_exception(function):
        def wrapper(schema, model):
            try:
                function(schema, model)
            except IntegrityError as e:
                error = f'Error: {e.orig}'
                return CommonResponses.bad_request_400(error)
            except TypeError as e:
                return CommonResponses.bad_request_400(e.args)
        return wrapper
