from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# standard starting statement
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dutylist.db'
app.config['SECRET_KEY'] = '511e2c5b14affa8183ea6833'
db = SQLAlchemy(app)


# [from DutyList import models2] used for creating db tables
from DutyList import routes2
