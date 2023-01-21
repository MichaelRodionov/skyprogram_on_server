from flask import Flask
from flask_restx import Api

from application.views.bookmarks import bookmark_ns
from application.views.posts import post_ns
from config import Config
from database.setup_db import db


api = Api()


# ----------------------------------------------------------------
# create app, register extensions, create tables
def create_app(config_object: Config):
    """
    This function is called to create Flask application
    :param config_object: Config
    :return: Flask application
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app: Flask):
    """
    This function is called to register extensions init database and create api
    :param app: Flask application
    """
    db.init_app(app)
    api.init_app(app)
    api.add_namespace(post_ns)
    api.add_namespace(bookmark_ns)
    create_data(app, db)


def create_data(app, database):
    """Creating table"""
    with app.app_context():
        database.create_all()


application = create_app(Config())


if __name__ == '__main__':
    application.run()
