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
    def browse(cls):
        # try:
        objs = []
        for obj in cls.query.all():
            objs.append(obj.to_dict)
        return json.dumps(objs)
        # except:
        #     return '', 400


    @classmethod
    def read(cls, id_param):
        # try:
        obj = cls.query.get(id_param)
        return json.dumps(obj.to_dict)
        # except:
        #     return '', 400


    @classmethod
    def edit(cls, id_param, data):
        # try:
        obj = cls.query.get(id_param)
        new = json.loads(data)

        if new['coordinate']['latitude']:
            obj.latitude = new['coordinate']['latitude']

        db.session.commit()
        return json.dumps(obj.to_dict)
        # except:
        #     return '', 400


    @classmethod
    def add(cls, data):
        # try:
        obj = cls.from_json(data)
        db.session.add(obj)
        db.session.commit()
        return json.dumps(obj.to_dict)
        # except:
        #     return '', 400


    @classmethod
    def delete(cls, id_param):
        # try:
        obj = cls.query.get(id_param)
        db.session.delete(obj)
        db.session.commit()
        return '', 204
        # except:
        #     return '', 400
