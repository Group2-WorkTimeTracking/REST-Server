import json
from datetime import *

from models.db import db
from models.account import Account
from models.note import Note
from models.timetag import TimeTag


class Employee(db.Model):
    id_emp = db.Column(db.Integer, primary_key=True)
    id_acc = db.Column(db.Integer, db.ForeignKey('account.id_acc'))
    id_loc = db.Column(db.Integer, db.ForeignKey('location.id_loc'))

    account = db.relationship('Account', uselist=False)
    location = db.relationship('Location', uselist=False)

    id_usr = db.Column(db.Integer, db.ForeignKey('user.id_usr'))

    def __init__(self, login, password, name, id_usr, id_loc):
        self.account = Account(login, password, name)
        self.id_usr = id_usr
        self.id_loc = id_loc

    @property
    def to_dict(self):
        return {
            'userId': self.id_emp,
            'realName': self.account.real_name,
            'login': self.account.login,
            'role': 'employee'
        }


    @classmethod
    def from_json(cls, data):
        obj = json.loads(data)
        return cls(obj['login'], obj['password'], obj['realName'], 1, 1)


    @classmethod
    def browse(cls):
        # try:
        objs = []
        for obj in cls.query.filter_by(id_usr=1).all():
            objs.append(obj.to_dict)
        return json.dumps(objs)
        # except:
        #     return '', 500


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
        #     return '', 500


    @classmethod
    def get_location(cls, id_param):
        # try:
        obj = cls.query.get(id_param)
        return json.dumps(obj.location.to_dict)
        # except:
        #     return '', 500


    @classmethod
    def set_location(cls, id_param, data):
        # try:
        obj = cls.query.get(id_param)
        json_data = json.loads(data)

        if 'locationId' in json_data:
            obj.id_loc = json_data['locationId']

        db.session.commit()
        return json.dumps(obj.location.to_dict)
        # except:
        #     return '', 500


    @classmethod
    def get_log(cls, id_param, pmonth=datetime.strftime(datetime.today(), '%Y-%m')):
        # try:
        month = datetime.strptime(pmonth, '%Y-%m')
        obj = {
            'month': datetime.strftime(month, '%Y-%m'),
            'totalWorkingHours': 0,
            'dailyWork': []
        }

        for nday in range(31):
            try:
                today = datetime(month.year, month.month, nday + 1)

                day = {
                    'day': datetime.strftime(today, '%Y-%m-%d'),
                    'workingHours': .0,
                    'note': ''
                }

                for x in Note.query.filter_by(id_emp=id_param).all():
                    if x.day_of_effectiveness.year == today.year and\
                            x.day_of_effectiveness.month == today.month and\
                            x.day_of_effectiveness.day == today.day:
                        day['note'] = x.message

                for y in TimeTag.query.filter_by(id_emp=id_param).all():
                    if y.timestamp.year == today.year and\
                            y.timestamp.month == today.month and\
                            y.timestamp.day == today.day:
                        if y.is_start:
                            day['workingHours'] -= (y.timestamp.timestamp() - today.timestamp())
                        else:
                            day['workingHours'] += (y.timestamp.timestamp() - today.timestamp())

                if day['workingHours'] != 0 or day['note'] != '':
                    day['workingHours'] /= 3600
                    obj['totalWorkingHours'] += day['workingHours']
                    obj['dailyWork'].append(day)
            except ValueError:
                pass

        return json.dumps(obj)
        # except:
        #     return '', 500
