from flask import Flask, render_template, redirect

from config import Config
from object import Object, db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route('/', methods=['GET'])  # GET is default
def display_table():
    with app.app_context():
        db.create_all()
        database_content = db.session.query(Object).all()
        return render_template('table.html', objects=database_content)


@app.route('/delete/<record_id>', methods=['POST'])
def delete_record(record_id):
    with app.app_context():
        db.session.delete(db.session.get(Object, record_id))
        db.session.commit()
        return redirect('/')


@app.route('/hello_world')
def hello_world():
    return 'Hello World!'
