import sqlalchemy as sa
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Object(db.Model):
    id = db.Column(sa.Integer, primary_key=True)
    categorical = db.Column(sa.Integer)
    continuous1 = db.Column(sa.Float)
    continuous2 = db.Column(sa.Float)
