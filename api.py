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
def display_table():
    with app.app_context():
        database_content = db.session.query(Object).all()
        return render_template('table.html', objects=database_content)


@app.route('/test')
def test():
    return 'Work in progress'
