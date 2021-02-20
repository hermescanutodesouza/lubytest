from app import ma
from models.model import Parent, Child
from marshmallow import fields


class ChildParentSchema(ma.SQLAlchemySchema):
    id = ma.auto_field()
    name = ma.auto_field()
    createdAt = fields.DateTime(format='%Y-%m-%d %H:%M:%S%z')
    updatedAt = fields.DateTime(format='%Y-%m-%d %H:%M:%S%z')

    class Meta:
        model = Parent
        ordered = True


class ChildSchema(ma.SQLAlchemySchema):
    id = ma.auto_field()
    name = ma.auto_field()
    createdAt = fields.DateTime(format='%Y-%m-%d %H:%M:%S%z')
    updatedAt = fields.DateTime(format='%Y-%m-%d %H:%M:%S%z')
    parent = ma.Nested(ChildParentSchema, many=True)

    class Meta:
        model = Child
        ordered = True


Child_schema = ChildSchema()
Children_schema = ChildSchema(many=True)
