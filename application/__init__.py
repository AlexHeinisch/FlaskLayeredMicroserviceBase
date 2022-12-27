from flask import Flask
from flask_cors import CORS

# Flask Injector
from flask_injector import FlaskInjector

# extensions
from application.extensions import custom_injector, db, migrate

# config loading
from application.config import load_config

# Dependency Injection config
from application.dependencies import configure

# Blueprints
from application.endpoint.message_endpoint import message
from application.endpoint.health_endpoint import health
from application.error.error_handlers import error_handlers


def create_app(test_config=None, injector_module=None) -> Flask:

    app = Flask(__name__)

    if test_config is None:
        app.config.from_object(load_config())
    else:
        app.config.from_mapping(test_config)

    print(app.config)

    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db) 

    app.register_blueprint(message, url_prefix='/message')
    app.register_blueprint(health, url_prefix='/health')
    app.register_blueprint(error_handlers)

    modules = [configure]
    if injector_module:
        modules.append(injector_module)

    FlaskInjector(app=app, modules=modules, injector=custom_injector)
    
    with app.app_context():
        db.create_all()
        return app
