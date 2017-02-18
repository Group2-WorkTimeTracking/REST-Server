import json

from models.db import db


class Location(db.Model):
    id_loc = db.Column(db.Integer, primary_key=True)
    name_loc = db.Column(db.String(255), unique=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    size_loc = db.Column(db.Float)

    id_usr = db.Column(db.Integer, db.ForeignKey('user.id_usr'))

    def __init__(self, name, lat, lon, size):
        self.name_loc = name
        self.latitude = lat
        self.longitude = lon
        self.size_loc = size

    @property
    def to_dict(self):
        return {
            'placeName': self.name_loc,
            'coordinate': {'latitude': self.latitude,
                           'longitude': self.longitude},
            'size': self.size_loc
        }


    @classmethod
    def from_json(cls, data):
        obj = json.loads(data)
        return cls(obj['placeName'],
                   obj['coordinate']['latitude'],
                   obj['coordinate']['longitude'],
                   obj['size'])


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
