import logging
import sys

from flask import Blueprint
from flask import Flask
from flask_restful import Api
from models.models import db
from config import Config
from resources.proxy import ProxyRouteResource
from resources.account import AccountResource
from resources.login import AccountLoginResource
from blueprints.accounts_page import accounts_page
from prometheus_flask_exporter import PrometheusMetrics

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))


def api_blueprint():
    api_bp = Blueprint('/', __name__)
    api = Api(api_bp)
    api.add_resource(ProxyRouteResource, '/')
    api.add_resource(AccountResource, '/account')
    api.add_resource(AccountLoginResource, '/login')
    return api_bp


def run_application(config):
    app = Flask('proxy', template_folder='templates')
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)
    app.config.from_object(config)
    app.register_blueprint(api_blueprint(), url_prefix='/')
    db.init_app(app)
    return app


if __name__ == "__main__":
    config = Config()
    app = run_application(config)
    app.register_blueprint(accounts_page)
    metrics = PrometheusMetrics(app=app)
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
