from flask import request

from src.apps.film.schemas import FilmGetSchema
from src.apps.film.models import CategoryModel
from src.apps.staff.models import StaffModel
from src.apps.film.utils import FilmUtils
from src.utils.responses import CommonResponses


class FilmServices:

    @staticmethod
    # @ExceptionsDecorator.integrity_exception
    def create(schema, model):
        data = request.get_json()
        obj_dict = schema.load(data)
        categories = FilmUtils.create_instance_relation(
            obj_dict['categories'], CategoryModel
        )
        staff = FilmUtils.create_instance_relation(
            obj_dict['staff'], StaffModel
        )
        obj = model(
            title=obj_dict['title'],
            description=obj_dict['description'],
            image=obj_dict['image'],
            stock=obj_dict['stock'],
            price=obj_dict['price'],
            availability=obj_dict['availability'],
            release_date=obj_dict['release_date'],
            film_type_id=obj_dict['film_type_id'],
            categories=categories,
            staff=staff
        )

        obj.save()
        result = FilmGetSchema().dump(obj)
        return CommonResponses.created_201(result)

    @staticmethod
    def update(id, schema, model):
        obj = model.get_by_id(id)
        if not obj:
            return CommonResponses.not_found_404()
        data = request.get_json()
        obj_dict = schema.load(data)
        model.query.filter_by(id=id).update({
            'title': obj_dict['title'],
            'description': obj_dict['description'],
            'image': obj_dict['image'],
            'stock': obj_dict['stock'],
            'price': obj_dict['price'],
            'availability': obj_dict['availability'],
            'release_date': obj_dict['release_date'],
            'film_type_id': obj_dict['film_type_id'],
            })

        FilmUtils.update_categories_relation(
            obj, obj_dict['categories'], CategoryModel
        )
        FilmUtils.update_staff_relation(obj, obj_dict['staff'], StaffModel)

        obj.save()
        result = FilmGetSchema().dump(obj)
        return CommonResponses.ok_200(result)
