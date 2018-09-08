import os
from flask import Flask

class Config:
    SECRET_KEY = 'grESrtgb284gvfnfd58437bhb'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("mutugieddie3@gmail.com")
    MAIL_PASSWORD = os.environ.get("winnieeddie321")
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
