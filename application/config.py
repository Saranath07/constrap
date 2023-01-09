import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LocalDevelopmentConfig(Config):
    SQLALCHEMY_DB_DIR = os.path.join(basedir, "/db_directory")
    SQLALCHEMY_DATABASE_URI = "sqlite:///project_example.sqlite3"
    DEBUG = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'constrapTS@gmail.com'
    MAIL_PASSWORD = 'vmlzdeaayffrguhe'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    