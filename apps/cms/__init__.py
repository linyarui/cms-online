from flask import Blueprint

cms = Blueprint('cms', __name__, url_prefix='/cms')

from apps.cms import views
