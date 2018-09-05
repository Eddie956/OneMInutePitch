from flask import Blueprints
main = Blueprint('main',__name__)
from . import views,errors