import json
import os
from flask import Flask, request, redirect

from models.db import db
from models.account import Account
from models.employee import Employee
from models.location import Location
from models.note import Note
from models.timetag import TimeTag
from models.user import User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db.init_app(app)

with app.app_context():
    # db.drop_all()
    db.create_all()


acc = User('jrandom', 'aStrongPassword', 'J. Random User')

loc = Location('OAMK, Kotkantie campus', 64.99958, 25.51078, 0.00220)

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
        },
        ...
    ]
}"""


@app.route('/')
def index():
    return redirect('/login', code=301)


@app.route('/login', methods=['POST'])
def login():
    return repr(acc)


@app.route('/account', methods=['GET', 'PUT'])
def account():
    if request.method == 'GET':
        return repr(acc)
    else:
        return repr(acc)


@app.route('/employee', methods=['GET', 'POST'])
def employee_account():
    if request.method == 'GET':
        return repr(acc)
    else:
        return repr(acc)


@app.route('/employee/<int:employee_id>', methods=['GET', 'PUT', 'DELETE'])
def employee_account_by_id(employee_id):
    if request.method == 'GET':
        return repr(acc)
    elif request.method == 'PUT':
        return repr(acc)
    else:
        return '', 204


@app.route('/location', methods=['GET', 'POST'])
def location():
    if request.method == 'GET':
        return repr(loc)

    else:
        try:
            locat = Location.from_json(request.data.decode())
        except:
            return '', 400

        return repr(locat)


@app.route('/location/<int:location_id>', methods=['GET', 'PUT', 'DELETE'])
def location_by_id(location_id):
    if request.method == 'GET':
        return repr(loc)
    elif request.method == 'PUT':
        return repr(loc)
    else:
        return '', 204


@app.route('/employee/<int:employee_id>/location', methods=['GET', 'PUT'])
def employee_location(employee_id):
    if request.method == 'GET':
        return repr(loc)
    elif request.method == 'PUT':
        return repr(loc)


@app.route('/employee/<int:employee_id>/logs', methods=['GET'])
def employee_logs(employee_id):
    return lgs


@app.route('/employee/<int:employee_id>/logs/<int:month_id>', methods=['GET'])
def employee_logs_per_month(employee_id, month_id):
    return lgs


@app.route('/account/location', methods=['GET'])
def account_location():
    return repr(loc)


@app.route('/work/start', methods=['POST'])
def start():
    try:
        timetag = TimeTag.from_json(request.data.decode(), True)
    except:
        return '', 400

    return json.dumps(timetag.json)


@app.route('/work/finish', methods=['POST'])
def finish():
    try:
        timetag = TimeTag.from_json(request.data.decode(), False)
    except:
        return '', 400

    return repr(timetag)


@app.route('/work/note', methods=['POST'])
def note():
    try:
        msg = Note.from_json(request.data.decode())
    except:
        return '', 400

    return json.dumps(msg.json)


@app.route('/account/logs', methods=['GET'])
def logs():
    return lgs


@app.route('/account/logs/<int:month_id>', methods=['GET'])
def logs_per_month(month_id):
    return lgs


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['PORT'])
