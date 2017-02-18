import json

from models.db import db
from models.account import Account


class Employee(db.Model):
    id_emp = db.Column(db.Integer, primary_key=True)
    id_acc = db.Column(db.Integer, db.ForeignKey('account.id_acc'))
    id_loc = db.Column(db.Integer, db.ForeignKey('location.id_loc'))

    account = db.relationship('Account', uselist=False)
    # logs = #something

    id_usr = db.Column(db.Integer, db.ForeignKey('user.id_usr'))

    def __init__(self, login, password, name, id_loc):
        self.account = Account(login, password, name)
        self.id_loc = id_loc

    @property
    def to_dict(self):
        return {
            'realName': self.account.real_name,
            'login': self.account.login,
            'role': 'employee'
        }


    @classmethod
    def from_json(cls, data):
        obj = json.loads(data)
        return cls(obj['login'], obj['password'], obj['realName'], 0)


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
