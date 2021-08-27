# import os

# class Config:
#         SECRET_KEY=os.environ.get('SECRET_KEY')
# 	MAIL_USERNAME='jumabarrak17@gmail.com'
#  	MAIL_PASSWORD='barry@1234'
#  	DATABASE_URL=''
# 	SQLALCHEMY_DATABASE_URL =''
import os

class Config:
    SECRET_KEY='54321'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://Access@localhost/ppitch'
    UPLOADED_PHOTOS_DEST='app/static/photos'
    # email configurations
    # MAIL_SERVER = 'stmp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}