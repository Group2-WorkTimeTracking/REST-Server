from models.db import db
from models.account import Account


class User(db.Model):
    id_usr = db.Column(db.Integer, primary_key=True)
    id_acc = db.Column(db.Integer, db.ForeignKey('account.id_acc'))

    account = db.relationship('Account', uselist=False)
    employees = db.relationship('Employee')
    places = db.relationship('Location')

    def __init__(self, login, password, name):
        self.account = Account(login, password, name)
        self.employees = []
        self.places = []

    @property
    def json(self):
        return {
            'realName': self.account.real_name,
            'login': self.account.login,
            'role': 'employer'
        }
