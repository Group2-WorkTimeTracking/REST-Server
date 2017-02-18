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
    def add(cls, data):
        # try:
        obj = cls.from_json(data)
        db.session.add(obj)
        db.session.commit()
        return json.dumps(obj.to_dict)
        # except:
        #     return '', 400
