from flask_migrate import Migrate
from flask_restful import Api

from app import create_app, getMarshmallow
from models import db
from resources.routes import set_routes


app = create_app()
ma = getMarshmallow(app)
migrate = Migrate(app, db)

api = Api(app)
set_routes(api)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")

