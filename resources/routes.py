from resources.Child import ChildListApi, ChildApi, ChildCreateApi
from resources.Parent import ParentApi, ParentsListApi, ParentCreateApi
from resources.healthcheck import HealthCheck


def set_routes(api):
    api.add_resource(HealthCheck, '/healthcheck')

    api.add_resource(ParentCreateApi, '/api/parent')
    api.add_resource(ParentsListApi, '/api/parents')
    api.add_resource(ParentApi, '/api/parent/<int:id>', endpoint="parent")

    api.add_resource(ChildCreateApi, '/api/child')
    api.add_resource(ChildListApi, '/api/children')
    api.add_resource(ChildApi, '/api/child/<int:id>')
