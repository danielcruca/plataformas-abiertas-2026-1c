from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os

mongo = PyMongo()

def create_app():

    load_dotenv()
    app = Flask(__name__)
    # URI en formato string (correcto)
    uri = os.getenv("MONGO_URI")     
    
    # Usar esta URI para Flask-PyMongo
    app.config["MONGO_URI"] = uri
    mongo.init_app(app)

    # También guardar el cliente de pymongo si usas current_app.config["MONGO_CLIENT"]
    app.config["MONGO_CLIENT"] = MongoClient(uri)

    CORS(app, origins="*")

    from .controllers.libros import libros_endpoints
    app.register_blueprint(libros_endpoints, url_prefix="/libreria/api/v1")

    return app
