import json
from datetime import datetime

from models.db import db


class TimeTag(db.Model):
    id_timetag = db.Column(db.Integer, primary_key=True)
    id_emp = db.Column(db.Integer, db.ForeignKey('employee.id_emp'))

    is_start = db.Column(db.Boolean)
    timestamp = db.Column(db.DateTime)

    def __init__(self, is_start, timestamp, id_emp):
        self.is_start = is_start
        self.timestamp = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')
        self.id_emp = id_emp

    @property
    def to_dict(self):
        return {
            'type': 'start' if self.is_start else 'stop',
            'timestamp': datetime.strftime(self.timestamp, '%Y-%m-%dT%H:%M:%S'),
            'userId': self.id_emp
        }


    @classmethod
    def from_json(cls, data, is_start):
        obj = json.loads(data)
        return cls(is_start, obj['timestamp'], obj['userId'])


    @classmethod
    def add(cls, data, is_start):
        # try:
        obj = cls.from_json(data, is_start)
        db.session.add(obj)
        db.session.commit()
        return json.dumps(obj.to_dict)
        # except:
        #     return '', 400
