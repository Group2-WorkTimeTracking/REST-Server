import json
import os
from flask import Flask, request, redirect
from flask_cors import CORS

from models.db import db
from models.account import Account
from models.user import User
from models.location import Location
from models.employee import Employee
from models.note import Note
from models.timetag import TimeTag


app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db.init_app(app)

with app.app_context():
    # db.drop_all()
    db.create_all()


lgs = """{
    "month": "2016-12",
    "totalWorkingHours": 142.1,
    "dailyWork": [
        {
            "day": "2016-12-01",
            "workingHours": 7.9,
            "note": ""
        },
        {
            "day": "2016-12-02",
            "workingHours": 8.3,
            "note": ""
        },
        {
            "day": "2016-12-05",
            "workingHours": 0.0,
            "note": "I have a meeting in Helsinki."
        }
    ]
}"""


@app.route('/')
def index():
    return redirect('/login', code=301)


@app.route('/login', methods=['POST'])
def login():
    return 501


@app.route('/account', methods=['GET', 'PUT'])
def account():
    if request.method == 'GET':
        return User.read(1)
    else:
        return User.edit(1, request.data)


@app.route('/employee', methods=['GET', 'POST'])
def employee_account():
    if request.method == 'GET':
        return Employee.browse()
    else:
        return Employee.add(request.data)


@app.route('/employee/<int:employee_id>', methods=['GET', 'PUT', 'DELETE'])
def employee_account_by_id(employee_id):
    if request.method == 'GET':
        return Employee.read(employee_id)
    elif request.method == 'PUT':
        return Employee.edit(employee_id, request.data)
    else:
        return Employee.delete(employee_id)


@app.route('/location', methods=['GET', 'POST'])
def location():
    if request.method == 'GET':
        return Location.browse()
    else:
        return Location.add(request.data)


@app.route('/location/<int:location_id>', methods=['GET', 'PUT', 'DELETE'])
def location_by_id(location_id):
    if request.method == 'GET':
        return Location.read(location_id)
    elif request.method == 'PUT':
        return Location.edit(location_id, request.data)
    else:
        return Location.delete(location_id)


@app.route('/employee/<int:employee_id>/location', methods=['GET', 'PUT'])
def employee_location(employee_id):
    if request.method == 'GET':
        return Employee.get_location(employee_id)
    else:
        return Employee.set_location(employee_id, request.data)


@app.route('/employee/<int:employee_id>/logs', methods=['GET'])
def employee_logs(employee_id):
    return Employee.get_log(employee_id)


@app.route('/employee/<int:employee_id>/logs/<month>', methods=['GET'])
def employee_logs_per_month(employee_id, month):
    return Employee.get_log(employee_id, month)


@app.route('/account/location', methods=['GET'])
def account_location():
    return Employee.get_location(1)


@app.route('/work/start', methods=['POST'])
def start():
    return TimeTag.add(request.data, True)


@app.route('/work/finish', methods=['POST'])
def finish():
    return TimeTag.add(request.data, False)


@app.route('/work/note', methods=['POST'])
def note():
    return Note.add(request.data)


@app.route('/account/logs', methods=['GET'])
def logs():
    return Employee.get_log(1)


@app.route('/account/logs/<month>', methods=['GET'])
def logs_per_month(month):
    return Employee.get_log(1, month)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['PORT'])
