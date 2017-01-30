import os
from flask import Flask, request

app = Flask(__name__)

o_account = """{...}"""

o_location = """{
    "place-name": "OAMK, Kotkantie campus",
    "coordinate": {"latitude": 64.99958,
                   "longitude": 25.51078},
    "size": 0.00220
}"""

o_logs = """{
    "month": "2016-12",
    "total-working-hours": 142.1,
    "daily-work": [
        {
            "day": "2016-12-01",
            "working-hours": 7.9,
            "note": ""
        },
        {
            "day": "2016-12-02",
            "working-hours": 8.3,
            "note": ""
        },
        {
            "day": "2016-12-05",
            "working-hours": 0.0,
            "note": "I have a meeting in Helsinki."
        },
        ...
    ]
}"""

o_timetag = """{
    "type": "start",
    "timestamp": 1485096644,
    "user-id": 42
}"""

o_note = """{
    "message": "I won’t be present because of a meeting in Helsinki.",
    "day-of-effectiveness": "2017-01-22",
    "user-id": 42
}"""


@app.route('/login', methods=['POST'])
def login():
    return o_account


@app.route('/account', methods=['GET', 'PUT'])
def account():
    if request.method == 'GET':
        return o_account
    else:
        return o_account


@app.route('/employee', methods=['GET', 'POST'])
def employee_account():
    if request.method == 'GET':
        return '[{}]'.format(o_account)
    else:
        return o_account


@app.route('/employee/<int:employee_id>', methods=['GET', 'PUT', 'DELETE'])
def employee_account_by_id(employee_id):
    if request.method == 'GET':
        return o_account
    elif request.method == 'PUT':
        return o_account
    else:
        return '', 204


@app.route('/location', methods=['GET', 'POST'])
def location():
    if request.method == 'GET':
        return '{}'.format(o_location)
    else:
        return o_location


@app.route('/location/<int:location_id>', methods=['GET', 'PUT', 'DELETE'])
def location_by_id(location_id):
    if request.method == 'GET':
        return o_location
    elif request.method == 'PUT':
        return o_location
    else:
        return '', 204


@app.route('/employee/<int:employee_id>/location', methods=['GET', 'PUT'])
def employee_location(employee_id):
    if request.method == 'GET':
        return o_location
    elif request.method == 'PUT':
        return o_location


@app.route('/employee/<int:employee_id>/logs', methods=['GET'])
def employee_logs(employee_id):
    return o_logs


@app.route('/employee/<int:employee_id>/logs/<int:month_id>', methods=['GET'])
def employee_logs_per_month(employee_id, month_id):
    return o_logs


@app.route('/account/location', methods=['GET'])
def account_location():
    return o_location


@app.route('/work/start', methods=['POST'])
def start():
    return o_timetag


@app.route('/work/finish', methods=['POST'])
def finish():
    return o_timetag

@app.route('/work/note', methods=['POST'])
def note():
    return o_note


@app.route('/account/logs', methods=['GET'])
def logs():
    return o_logs


@app.route('/account/logs/<int:month_id>', methods=['GET'])
def logs_per_month(month_id):
    return o_logs


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['PORT'])
