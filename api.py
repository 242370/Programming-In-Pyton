from flask import Flask, render_template, request
from config import Config
from flask_sqlalchemy import SQLAlchemy

from object import Object, db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():
    with app.app_context():
        ids = ''
        categoricals = ''
        continuous1 = ''
        continuous2 = ''
        row_count = 0

        database_content = db.session.query(Object).all()
        for object in database_content:
            ids = ids + str(object.id)
            categoricals = categoricals + str(object.categorical)
            continuous1 = continuous1 + str(object.continuous1)
            continuous2 = continuous2 + str(object.continuous2)
            row_count += 1

        return render_template('table.html', row_count=row_count, ID=ids, categorical=categoricals
                               , continuous1=continuous1, continuous2=continuous2)


@app.route('/test')
def test():
    return 'Work in progress'
