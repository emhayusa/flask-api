from flask_restplus import Api
from flask import Blueprint

from .main.controller.news_controller import api as news_ns


blueprint = Blueprint('api', __name__, url_prefix='/api-salatiga')

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(blueprint,
          title='FLASK RESTPLUS API FOR SALATIGA SMART CITY',
          version='1.0',
          description='a flask restplus web service for SALATIGA SMART CITY',
          authorizations=authorizations,
          security='apikey',
          )

api.add_namespace(news_ns, path='/news')

