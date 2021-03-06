# The application constructor.
from flask import Flask
from config import config
# from flask_bootstrap import Bootstrap

# bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # bootstrap.init_app(app)

    # register the blueprint to the application
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
