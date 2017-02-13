import json

from models.db import db


class Location(db.Model):
    id_loc = db.Column(db.Integer, primary_key=True)
    name_loc = db.Column(db.String(255), unique=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    size_loc = db.Column(db.Float)

    id_usr = db.Column(db.Integer, db.ForeignKey('user.id_usr'))

    @classmethod
    def from_json(cls, data):
        obj = json.loads(data)
        return cls(obj['placeName'],
                   obj['coordinate']['latitude'],
                   obj['coordinate']['longitude'],
                   obj['size'])

    def __init__(self, name, lat, lon, size):
        self.name_loc = name
        self.latitude = lat
        self.longitude = lon
        self.size_loc = size

    def __repr__(self):
        return json.dumps({
            'placeName': self.name_loc,
            'coordinate': {'latitude': self.latitude,
                           'longitude': self.longitude},
            'size': self.size_loc
        })
