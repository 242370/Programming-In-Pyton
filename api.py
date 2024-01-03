import json
import requests as requests
from flask import Flask, render_template, redirect, request

from config import Config
from object import Object, db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route('/', methods=['GET'])
def display_table():
    db.create_all()
    database_content = db.session.query(Object).all()
    return render_template('table.html', objects=database_content)


@app.route('/delete/<record_id>', methods=['POST'])
def delete_record(record_id):
    record_to_be_deleted = db.session.get(Object, record_id)
    if record_to_be_deleted is None:
        return redirect('/error/404/no such record')

    record_to_be_deleted.delete()
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
        return redirect('/error/400/categorical must be integer greater than 0')
    if not isinstance(continuous1, float):
        return redirect('/error/400/continuous must be a floating point number')
    if not isinstance(continuous2, float):
        return redirect('/error/400/continuous must be a floating point number')

    new_object = Object(categorical=categorical, continuous1=continuous1, continuous2=continuous2)
    new_object.add_new()
    return redirect('/')


@app.route('/error/<error_code>/<error_message>')
def display_error_page(error_code, error_message):
    return render_template('error.html', error_code=error_code, error_message=error_message), error_code


@app.route('/api/data', methods=['GET'])
def api_get_data():
    json_dicts = []

    db.create_all()
    database_content = db.session.query(Object).all()

    for object in database_content:
        json_dict = {'id': object.id, 'categorical': object.categorical, 'continuous1': object.continuous1, 'continuous2': object.continuous2}
        json_dicts.append(json_dict)

    return json_dicts


@app.route('/api/data', methods=['POST'])
def api_post_data():
    new_object_json = request.json
    categorical = new_object_json.get('categorical')
    continuous1 = new_object_json.get('continuous1')
    continuous2 = new_object_json.get('continuous2')

    if not isinstance(categorical, int) or categorical < 1:
        return {'error': 'categorical is incorrect'}, 400
    if not isinstance(continuous1, float):
        return {'error': 'continuous1 is incorrect'}, 400
    if not isinstance(continuous2, float):
        return {'error': 'continuous2 is incorrect'}, 400

    new_object = Object(categorical=categorical, continuous1=continuous1, continuous2=continuous2)
    new_object.add_new()
    return {'new_object_id': new_object.id}


@app.route('/api/data/<record_id>', methods=['DELETE'])
def api_delete_data(record_id):
    record_to_be_deleted = db.session.get(Object, record_id)
    if record_to_be_deleted is None:
        return {'error': 'no object with such index in the database'}, 404

    record_to_be_deleted.delete()
    return {'deleted_object_id': record_id}


# api testing
if __name__ == '__main__':
    print('DELETE FROM WEB PART TESTING WITH INVALID INDEX')
    r = requests.post('http://127.0.0.1:5000/delete/100')
    print('Message: ' + str(r.content))
    print('\n')
    print('GET TESTING')
    r = requests.get('http://127.0.0.1:5000/api/data')
    print('GET status code: ' + str(r.status_code))
    print('GET content: ' + str(r.content))
    print('\n')
    print('POST TESTING')
    r = requests.post('http://127.0.0.1:5000/api/data', data=json.dumps({'categorical': 1, 'continuous1': 1.0, 'continuous2': 2.0}),
                      headers={'Content-Type': 'application/json'})
    print('POST status code with valid data: ' + str(r.status_code))
    print('Added ID: ' + str(r.content))
    r = requests.post('http://127.0.0.1:5000/api/data', data=json.dumps({'categorical': 0, 'continuous1': 1.0, 'continuous2': 2.0}),
                      headers={'Content-Type': 'application/json'})
    print('POST status code with invalid data: ' + str(r.status_code))
    print('Message: ' + str(r.content))
    print('\n')
    print('DELETE TESTING')
    r = requests.delete('http://127.0.0.1:5000/api/data/8')
    print('DELETE status code with valid request: ' + str(r.status_code))
    print('Deleted ID: ' + str(r.content))
    r = requests.delete('http://127.0.0.1:5000/api/data/100')
    print('DELETE status code with invalid request: ' + str(r.status_code))
    print('Message: ' + str(r.content))
