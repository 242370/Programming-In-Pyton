import json

from flask import Flask, render_template, redirect, request

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


@app.route('/delete/<record_id>', methods=['POST', 'GET'])
def delete_record(record_id):
    with app.app_context():
        record_to_be_deleted = db.session.get(Object, record_id)
        if record_to_be_deleted is None:
            return redirect('/error/404')

        db.session.delete(record_to_be_deleted)
        db.session.commit()
        return redirect('/')


@app.route('/add', methods=['GET'])
def display_adding_form():
    return render_template('form.html')


@app.route('/add', methods=['POST'])
def add_record():
    categorical = request.form.get('categorical', type=int)
    continuous1 = request.form.get('continuous1', type=float)
    continuous2 = request.form.get('continuous2', type=float)

    if not isinstance(categorical, int) or categorical < 1:
        return redirect('/error/400')
    if not isinstance(continuous1, float):
        return redirect('/error/400')
    if not isinstance(continuous2, float):
        return redirect('/error/400')

    new_object = Object(categorical=categorical, continuous1=continuous1, continuous2=continuous2)
    with app.app_context():
        db.session.add(new_object)
        db.session.commit()
        return redirect('/')


@app.route('/error/<error_code>')
def display_error_page(error_code):
    return render_template('error.html', error_code=error_code), error_code


@app.route('/api/data', methods=['GET'])
def api_get_data():
    json_dicts = []

    with app.app_context():
        db.create_all()
        database_content = db.session.query(Object).all()

    for object in database_content:
        json_dict = {'id': object.id, 'categorical': object.categorical, 'continuous1': object.continuous1, 'continuous2': object.continuous2}
        json_dicts.append(json_dict)

    json_data = json.dumps(json_dicts, indent=4)
    return json_data
