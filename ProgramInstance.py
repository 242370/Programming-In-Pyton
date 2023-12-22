from Zad2 import Zad2
from object import Object
from api import app, db

if __name__ == '__main__':
    # simulation = Zad2()
    # simulation.start_simulation()
    object = Object(categorical=1, continuous1=1.0, continuous2=2.0)
    with app.app_context():
        db.create_all()
        db.session.add(object)
        db.session.commit()
        object = None
        object = db.session.get(Object, 1)
    print(object)
