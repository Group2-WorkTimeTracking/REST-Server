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

    def __repr__(self):
        return json.dumps({
            'realName': self.account.real_name,
            'login': self.account.login,
            'role': 'employee'
        })
