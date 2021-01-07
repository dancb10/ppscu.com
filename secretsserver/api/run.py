from flask import Flask
from models import db
from flask import Blueprint
from flask_restful import Api
from resources.account import AccountResource
from resources.login import AccountLoginResource
from resources.secret import SecretResource

def api_blueprint():
    api_bp = Blueprint('api', __name__)
    api = Api(api_bp)
    api.add_resource(AccountResource, '/account')
    api.add_resource(AccountLoginResource, '/login')
    api.add_resource(SecretResource, '/secret')
    return api_bp

def run_application(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(api_blueprint(), url_prefix='/api')
    db.init_app(app)
    return app

if __name__ == "__main__":
    app = run_application("config")
    app.run(debug=True)
