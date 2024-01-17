import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# Get the absolute path of the script's directory
script_directory = os.path.abspath(os.path.dirname(__file__))

# Navigate one level up to the parent directory and then to the 'data' folder
database_path = os.path.join(script_directory, '..', 'data', 'db.sqlite')

# Configure the Flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Import route modules after initializing app, db, and ma
from api.routes import voucher_routes
from api.routes import redeem_routes
