from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configire_uploads,IMAGES
from flask_email import Mail

bootstrap=Bootstrap(app)
db=SQLAlchemy()
photos=UploadSet('photos',IMAGES)
mail=Mail()


def create_app(config_name):

    # Initializing application
    app = Flask(__name__)

    #initializing login
    login_manager = LoginManager()
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'


    #registration of the blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    #initializing Mail
     mail.init_app(app)

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # configure UploadSet
    configure_uploads(app,photos)

    #Register the blueprint 
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting config
    from .requests import configure_request
    configure_request(app)

    
    return app