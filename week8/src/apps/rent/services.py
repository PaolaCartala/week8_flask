from flask import request

from src.utils.responses import CommonResponses
from src.utils.decorators import ExceptionsDecorator
from src.apps.rent.utils import RentUtils


class RentServices:

    @staticmethod
    # @ExceptionsDecorator.integrity_exception
    def create(schema, model):
        data = request.get_json()
        obj_dict = schema.load(data)
        obj = model(**obj_dict)
        RentUtils.create_debt(obj, obj_dict)
        obj.save()
        RentUtils.update_availability_substract(obj)
        result = schema.dump(obj)
        return CommonResponses.created_201(result)

    @staticmethod
    def update(id, schema, model):
        obj = model.get_by_id(id)
        if not obj:
            return CommonResponses.not_found_404()
        data = request.get_json()
        obj_dict = schema.load(data)
        model.query.filter_by(id=id).update(obj_dict)
        RentUtils().update_debt(obj)
        obj.save()
        RentUtils.update_availability_add(obj)
        result = schema.dump(obj)
        return CommonResponses.ok_200(result)
