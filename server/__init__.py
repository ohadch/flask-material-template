from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from server.settings import UPLOAD_FOLDER, VERSION, POSTGRES_URI, STATIC_FOLDER, TEMPLATE_FOLDER
from server.logger import logger

# initialize flask application
app = Flask(__name__,
            static_folder=STATIC_FOLDER,
            template_folder=TEMPLATE_FOLDER)

app.config["SQLALCHEMY_DATABASE_URI"] = POSTGRES_URI
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

logger.info(f"App version: {VERSION}")


db = SQLAlchemy(app)
jwt = JWTManager(app)