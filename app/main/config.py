import os


# uncomment the line below for postgres database url from environment variable
CONNECTION_SERVER = os.getenv('CONNECTION_SERVER', 'localhost')
CONNECTION_PORT = os.getenv('CONNECTION_PORT', '5432')
CONNECTION_USER = os.getenv('CONNECTION_USER', 'postgres')
CONNECTION_PASSWORD = os.getenv('CONNECTION_PASSWORD', 'password')

DB_URL='{server}:{port}'.format(server=CONNECTION_SERVER,port=CONNECTION_PORT)
DB_DEV="api_salatiga"
DB_PROD="api_ppig_prod"
DB_TEST="api_ppig_test"

DB_URL_DEV = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=CONNECTION_USER,pw=CONNECTION_PASSWORD,url=DB_URL,db=DB_DEV)
DB_URL_PROD = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=CONNECTION_USER,pw=CONNECTION_PASSWORD,url=DB_URL,db=DB_PROD)
DB_URL_TEST = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=CONNECTION_USER,pw=CONNECTION_PASSWORD,url=DB_URL,db=DB_TEST)


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_pr3cious_secret_key_pp1g')
    DEBUG = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    SQLALCHEMY_DATABASE_URI = DB_URL_DEV
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = DB_URL_TEST 
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    SQLALCHEMY_DATABASE_URI = DB_URL_PROD


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY