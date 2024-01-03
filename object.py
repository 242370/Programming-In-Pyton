import sqlalchemy as sa
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Object(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categorical = db.Column(db.Integer)
    continuous1 = db.Column(db.Float)
    continuous2 = db.Column(db.Float)
