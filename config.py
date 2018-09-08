import os
from flask import Flask

class Config:
    SECRET_KEY = 'grESrtgb284gvfnfd58437bhb'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
class ProdConfig(Config):
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://a:mango@localhost/oneminute'

    DEBUG = True

class TestConfig(Config):
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig
}
