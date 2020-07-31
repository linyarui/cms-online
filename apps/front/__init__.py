from flask import Blueprint

front = Blueprint('front', __name__)

from apps.front import views
