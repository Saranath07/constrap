import os
from flask import Flask
from flask_restful import Api
from application.config import LocalDevelopmentConfig
from application.database import db
from flask_mail import Mail, Message



app = None
api = None
def create_app():
    
    app = Flask(__name__)
    if os.getenv("ENV","development") == "production":
        raise Exception("Currently no production config is setup.")
    else:
        print("Starting Local Development")
        app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    api = Api(app)
    app.app_context().push()
    return app, api

app, api = create_app()
with app.app_context():
    db.create_all()

mail = Mail(app)






from application.login_controllers import *

from application.user_controllers import *




if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)