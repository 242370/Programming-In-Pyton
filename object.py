import sqlalchemy as sa
import sqlalchemy.orm as so
from api import db


class Object(db.Model):
    def __init__(self, categorical, continuous1, continuous2):
        self.id: so.Mapped[int] = so.mapped_column(primary_key=True)
        self.categorical: so.Mapped[int] = so.mapped_column(sa.INT)
        self.continuous1: so.Mapped[float] = so.mapped_column(sa.FLOAT)
        self.continuous2: so.Mapped[float] = so.mapped_column(sa.FLOAT)

    def to_string(self):
        return 'Object ' + self.id + '/n' + 'categorical: ' + self.categorical
