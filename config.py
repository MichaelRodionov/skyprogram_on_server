from os import path


# ----------------------------------------------------------------
# configuration class
class Config:
    path = path.abspath(path.join("database", "posts.db"))
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{path}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_PRETTYPRINT_REGULAR = True
    JSON_AS_ASCII = False
    DEBUG = False
