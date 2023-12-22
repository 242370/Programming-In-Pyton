import sqlalchemy as sa
import sqlalchemy.orm as so
from api import db, app


class Object(db.Model):
    id = db.Column(sa.Integer, primary_key=True)
    categorical = db.Column(sa.Integer)
    continuous1 = db.Column(sa.Float)
    continuous2 = db.Column(sa.Float)
