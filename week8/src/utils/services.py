from flask import request

from src.utils.responses import CommonResponses
from src.utils.decorators import ExceptionsDecorator


class CommonServices:

    @staticmethod
    def list(schema, model):
        obj = model.get_all()
        result = schema.dump(obj, many=True)
        return CommonResponses.ok_200(result)

    @staticmethod
    # @ExceptionsDecorator.integrity_exception
    def create(schema, model):
        data = request.get_json()
        obj_dict = schema.load(data)
        obj = model(**obj_dict)
        obj.save()
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
        obj.save()
        result = schema.dump(obj)
        return CommonResponses.ok_200(result)

    @staticmethod
    def destroy(id, model):
        obj = model.get_by_id(id)
        if not obj:
            return CommonResponses.not_found_404()
        obj.delete()
        return CommonResponses.no_content_204()
