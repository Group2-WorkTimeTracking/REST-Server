import json
from datetime import datetime

from models.db import db


class Note(db.Model):
    id_note = db.Column(db.Integer, primary_key=True)
    id_emp = db.Column(db.Integer, db.ForeignKey('employee.id_emp'))

    message = db.Column(db.String(255))
    day_of_effectiveness = db.Column(db.DateTime)

    def __init__(self, message, effectivness, id_emp):
        self.message = message
        self.day_of_effectiveness = datetime.strptime(effectivness, '%Y-%m-%d')
        self.id_emp = id_emp

    @property
    def to_dict(self):
        return {
            'message': self.message,
            'day-of-effectiveness':
                datetime.strftime(self.day_of_effectiveness, '%Y-%m-%d'),
            'userId': self.id_emp
        }


    @classmethod
    def from_json(cls, data):
        obj = json.loads(data)
        return cls(obj['message'], obj['dayOfEffectiveness'], obj['userId'])


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
