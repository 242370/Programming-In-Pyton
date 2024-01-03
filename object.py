from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Object(db.Model):
    id = db.mapped_column(db.Integer, primary_key=True)
    categorical = db.mapped_column(db.Integer)
    continuous1 = db.mapped_column(db.Float)
    continuous2 = db.mapped_column(db.Float)

    def add_new(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
