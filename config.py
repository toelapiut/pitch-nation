import os

class Config:

    SECRET_KEY = os.environ.get('qwerty12')
    UPLOADED_PHOTOS_DEST='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'pitchnation'
    MAIL_USERNAME = os.environ.get("toelapiut7@gmail.com")
    MAIL_PASSWORD = os.environ.get("Kinyanjui123")

class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    

class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://toel:KingChase@localhost/pitchnation'
    DEBUG = True    

config_options = {
'development':DevConfig,
'production':ProdConfig
}