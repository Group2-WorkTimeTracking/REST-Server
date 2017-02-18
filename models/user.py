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
    def read(cls, id_param):
        # try:
        obj = cls.query.get(id_param)
        return json.dumps(obj.to_dict)
        # except:
        #     return '', 404


    @classmethod
    def edit(cls, id_param, data):
        # try:
        obj = cls.query.get(id_param)
        new = json.loads(data)

        if 'login' in new:
            obj.account.login = new['login']

        if 'password' in new:
            obj.account.passwd = new['password']

        if 'realName' in new:
            obj.account.real_name = new['realName']

        db.session.commit()
        return json.dumps(obj.to_dict)
        # except:
        #     return '', 400
