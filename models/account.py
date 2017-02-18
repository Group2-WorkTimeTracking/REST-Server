import hashlib

from models.db import db


class Account(db.Model):
    id_acc = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(128))
    real_name = db.Column(db.String(255))

    def __init__(self, login, password, name):
        self.login = login
        self.passwd = password
        self.real_name = name

    @property
    def passwd(self):
        return ''

    @passwd.setter
    def passwd(self, value):
        self.password = enc_pw(value)


def enc_pw(password):
    return hashlib.sha3_512(password.encode()).hexdigest()
