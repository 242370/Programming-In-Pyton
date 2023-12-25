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
        result = ''
        row_count = 0
        database_content = db.session.query(Object).all()
        for object in database_content:
            result = result + str(object.id)
            row_count += 1

        column_count = 4

        return render_template('table.html', row_count=row_count, column_count=column_count, xD=result)


@app.route('/test')
def test():
    return 'Work in progress'
