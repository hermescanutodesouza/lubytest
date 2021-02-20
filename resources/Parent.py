from flask import Response, request
from flask_restful import Resource, reqparse
from sqlalchemy.sql import text

import json

from app import db
from models.model import Parent, Child, parent_child
from serializers.Parent import Parents_schema, Parent_schema
from util.common import notfound, deleted


class ParentsListApi(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('children', type=int, help='must be a int')
        args = parser.parse_args()
        print(args['children'])
        if args['children'] is not None:
            sql = """select 
                    p2.* ,	
                    count(pc.child_id) as "total"
                    from parent_child pc 
                    right join parent p2 on p2.id = pc.parent_id
                    group by  (p2.id,pc.parent_id)
                    having count(pc.child_id) = {}
                    order by parent_id;""".format(args['children'])
            rs = db.engine.execute(text(sql))
            id = []
            for i in rs:
                id.append(i[0])
            parents = db.session.query(Parent).filter(Parent.id.in_(id)).all()
        else:
            parents = Parent.query.order_by(Parent.id).all()
        if len(parents) > 0:
            return Response(Parents_schema.dumps(parents), mimetype="application/json", status=200)
        else:
            return notfound


class ParentCreateApi(Resource):
    def post(self):
        error = False
        request_json = request.get_json(silent=True)
        name: str = request_json['name']
        parent = Parent(name=name)
        parent.save()
        last = ""
        if 'child' in request_json:
            child = request_json['child']
            for item in child:
                if 'name' in item:
                    c = Child(name=item['name']).save()
                    parent.child.append(c)
                if 'id' in item:
                    c = Child.query.filter_by(id=item['id']).first()
                    if c and c.parent.count() < 2 and last != item['id']:
                        parent.child.append(c)
                        last = item['id']
                    # else:
                    #     error = ',"error":"child has 2 parents or duplicated child id"}'
            db.session.commit()
        r = Parent_schema.dumps(parent)
        # if error:
        #     r = r.replace('"child"', error)
        return Response(r, mimetype="application/json", status=201)


class ParentApi(Resource):
    def get(self, id):
        parent = Parent.query.filter_by(id=id).first()
        parser = reqparse.RequestParser()

        if parent:
            return Response(Parent_schema.dumps(parent), mimetype="application/json", status=200)
        else:
            return notfound

    def put(self, id):
        parent = Parent.query.filter_by(id=id).first()
        if parent:
            request_json = request.get_json(silent=True)
            parent.name = request_json['name']
            parent.save()
            return Response(Parent_schema.dumps(parent), mimetype="application/json", status=200)
        else:
            return notfound

    def delete(self, id):
        parent = Parent.query.filter_by(id=id).first()
        if parent:
            parent.remove()
            return deleted
        else:
            return notfound
