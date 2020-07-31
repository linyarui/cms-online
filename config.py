import os
from datetime import timedelta


class Config:
    ERROR_404_HELP = False

    SECRET_KEY = os.getenv('APP_SECRET', 'secret key')

    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_HOST = '127.0.0.1'
    DB_PORT = '3306'
    DB_NAME = 'cms_online'

    DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 100
    CSRF_ENABLED = True

    USER_ID = 'USERID'
    CMS_USER_ID = 'CMSUSERID'
    PERMANENT_SESSION_LIFETIME = timedelta(seconds=6 * 60 * 60)


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    TESTING = True
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False


config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig
}
