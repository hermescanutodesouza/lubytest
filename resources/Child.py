from flask import Response, request
from flask_restful import Resource, reqparse
from sqlalchemy.sql import text

from app import db
from models.model import Child, Parent
from serializers.Child import Child_schema, Children_schema
from util.common import notfound, deleted


class ChildListApi(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('parents', type=int, help='must be a int')
        args = parser.parse_args()
        if args['parents'] is not None:
            sql = """select  c.*,
                count(pc.child_id) as "total"
                from parent_child pc 
                right join child c on c.id = pc.child_id
                group by (c.id,pc.child_id)
                having count(pc.parent_id) = {}
                order by child_id;""".format(args['parents'])
            rs = db.engine.execute(text(sql))
            id = []
            for i in rs:
                id.append(i[0])
            children = db.session.query(Child).filter(Child.id.in_(id)).all()
        else:
            children = Child.query.order_by(Child.id).all()
        if len(children) > 0:
            return Response(Children_schema.dumps(children), mimetype="application/json", status=200)
        else:
            return notfound


class ChildCreateApi(Resource):
    def post(self):
        error = False
        request_json = request.get_json(silent=True)
        name: str = request_json['name']
        child = Child(name=name)
        child.save()
        last = ""
        if 'parent' in request_json:
            parent = request_json['parent']
            a = 0
            for item in parent:
                if 'name' in item:
                    p = Parent(name=item['name']).save()
                    child.parent.append(p)
                    a += 1
                if 'id' in item:
                    p = Parent.query.filter_by(id=item['id']).first()
                    if p and last != item['id']:
                        child.parent.append(p)
                        last = item['id']
                        a += 1
                if a == 2:
                    # error = '"error":"A child can have up to two parents or duplicated parent","parent"'
                    break

        db.session.commit()
        r = Child_schema.dumps(child)
        # if error:
        #     r = r.replace('"parent"', error)
        return Response(r, mimetype="application/json", status=201)


class ChildApi(Resource):
    def get(self, id):
        child = Child.query.filter_by(id=id).first()
        if child:
            return Response(Child_schema.dumps(child), mimetype="application/json", status=200)
        else:
            return notfound

    def put(self, id):
        child = Child.query.filter_by(id=id).first()
        if child:
            request_json = request.get_json(silent=True)
            child.name = request_json['name']
            child.save()
            return Response(Child_schema.dumps(child), mimetype="application/json", status=200)
        else:
            return notfound

    def delete(self, id):
        child = Child.query.filter_by(id=id).first()
        if child:
            child.remove()
            return deleted
        else:
            return notfound
