import json

class TimeTag:

    def __init__(self, tag_type, timestamp, user_id):
        self.tag_type = 'stop' if tag_type == 'stop' else 'start'
        self.timestamp = timestamp
        self.user_id = user_id


    @classmethod
    def from_json(cls, data, kind):
        obj = json.loads(data)
        return cls(kind, obj['timestamp'], obj['userId'])


    def __repr__(self):
        return json.dumps({
            'type': self.tag_type,
            'timestamp': self.timestamp,
            'userId': self.user_id
        })



class Note:

    def __init__(self, message, effectivness, user_id):
        self.message = message
        self.effectivness = effectivness
        self.user_id = user_id


    @classmethod
    def from_json(cls, data):
        obj = json.loads(data)
        return cls(obj['message'], obj['dayOfEffectiveness'], obj['userId'])


    def __repr__(self):
        return json.dumps({
            'message': self.message,
            'day-of-effectiveness': self.effectivness,
            'userId': self.user_id
        })
