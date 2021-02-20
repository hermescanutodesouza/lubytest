from app import ma
from models.model import Parent, Child
from marshmallow import  fields


# class ParentSchema(ma.Schema):
#     class Meta:
#         fields = ("id", "name", "createdAt", "updatedAt")
#
#
# Parent_schema = ParentSchema()
# Parents_schema = ParentSchema(many=True)
#
#
# from app.app import ma
# from models.model import Parent, Child

class ParentChildSchema(ma.SQLAlchemyAutoSchema):
    id = ma.auto_field()
    name = ma.auto_field()
    createdAt = fields.DateTime(format='%Y-%m-%d %H:%M:%S%z')
    updatedAt = fields.DateTime(format='%Y-%m-%d %H:%M:%S%z')

    class Meta:
        model = Child
        ordered = True


class ParentSchema(ma.SQLAlchemyAutoSchema):
    id = ma.auto_field()
    name = ma.auto_field()
    createdAt = fields.DateTime(format='%Y-%m-%d %H:%M:%S%z')
    updatedAt = fields.DateTime(format='%Y-%m-%d %H:%M:%S%z')
    child = ma.Nested(ParentChildSchema, many=True)

    class Meta:
        model = Parent
        ordered = True


Parent_schema = ParentSchema()
Parents_schema = ParentSchema(many=True)
