from flask import Blueprint
from flask_restful import Api

bp = Blueprint('api', __name__)
restful_api = Api(bp)

from app.api import beer

restful_api.add_resource(beer.Beer, '/beer')