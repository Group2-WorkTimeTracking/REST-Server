import json

from models.db import db


class Note(db.Model):
    id_note = db.Column(db.Integer, primary_key=True)
    id_emp = db.Column(db.Integer, db.ForeignKey('employee.id_emp'))

    message = db.Column(db.String(255))
    day_of_effectiveness = db.Column(db.String(10))

    @classmethod
    def from_json(cls, data):
        obj = json.loads(data)
        return cls(obj['message'], obj['dayOfEffectiveness'], obj['userId'])

    def __init__(self, message, effectivness, id_emp):
        self.message = message
        self.effectivness = effectivness
        self.id_emp = id_emp

    def __repr__(self):
        return json.dumps({
            'message': self.message,
            'day-of-effectiveness': self.effectivness,
            'userId': self.user_id
        })
