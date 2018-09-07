import os
from flask import Flask

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://a:mango@localhost/oneminute'
    SECRET_KEY = 'grESrtgb284gvfnfd58437bhb'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig
}
