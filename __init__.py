#initialises the application  registers the routes from the routes.py file.

from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register the blueprint (for routes)
    from .routes import main
    app.register_blueprint(main)

    return app
