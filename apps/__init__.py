from flask import Flask
from exts import db
from exts import mail
from config import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config['development'])

    db.init_app(app)
    mail.init_app(app)

    from apps.cms import cms as cms_blueprint
    app.register_blueprint(cms_blueprint)
    from apps.common import common as common_blueprint
    app.register_blueprint(common_blueprint)
    from apps.front import front as front_blueprint
    app.register_blueprint(front_blueprint)

    return app


