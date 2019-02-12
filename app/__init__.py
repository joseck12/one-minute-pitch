
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config_options
from flask_login import LoginManager


db = SQLAlchemy()
# bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.enter'

def create_app(config_name):

   app = Flask(__name__)

   # Creating the app configurations
   app.config.from_object(config_options[config_name])

   # Initializing flask extensions
   db.init_app(app)
   bootstrap = Bootstrap(app)
   login_manager.init_app(app)

   # Registering the blueprint
   from .main import main as main_blueprint
   app.register_blueprint(main_blueprint)
   # from .auth import auth as auth_blueprint
   # app.register_blueprint(auth_blueprint,url_prefix = '')

   return app
