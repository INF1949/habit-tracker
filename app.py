import os
from flask import Flask
from routes import pages
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()  # loads content of .env into the program's system environment so uri can be used



def create_app():   #factory function to create the application
    app = Flask(__name__)
    app.register_blueprint(pages)
    client=MongoClient(os.environ.get("MONGODB_URI"))
    app.db=client.get_default_database()

    return app
