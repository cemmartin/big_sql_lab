from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user@localhost:5432/coffeeshop" 

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.customer import Customer
from models.drink import Drink
from controllers.drink_controller import drink_blueprint

app.register_blueprint(drink_blueprint)

