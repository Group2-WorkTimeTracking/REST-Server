import json

from models.db import db
from models.account import Account


class User(db.Model):
    id_usr = db.Column(db.Integer, primary_key=True)
    id_acc = db.Column(db.Integer, db.ForeignKey('account.id_acc'))

    account = db.relationship('Account', uselist=False)
    employees = db.relationship('models.employee.Employee')
    places = db.relationship('models.location.Location')

    def __init__(self, login, password, name):
        self.account = Account(login, password, name)
        self.employees = []
        self.places = []

    @property
    def to_dict(self):
        return {
            'realName': self.account.real_name,
            'login': self.account.login,
            'role': 'employer'
        }


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
