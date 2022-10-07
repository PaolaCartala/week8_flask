
class FilmUtils:

    @staticmethod
    def create_instance_relation(data, model):
        instances = []
        for item_id in data:
            instances.append(model.simple_filter(id=item_id))
        return instances

    @staticmethod
    def update_categories_relation(obj, data, model):
        obj.categories = []
        obj.commit()
        for item_id in data:
            obj.categories.append(model.simple_filter(id=item_id))
            obj.commit()

    @staticmethod
    def update_staff_relation(obj, data, model):
        obj.staff = []
        obj.commit()
        for item_id in data:
            obj.staff.append(model.simple_filter(id=item_id))
            obj.commit()
