import json

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
