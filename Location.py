import json

class Location:

    def __init__(self, place_name, latitude, longitude, size):
        self.place_name = place_name
        self.latitude = latitude
        self.longitude = longitude
        self.size = size


    def __repr__(self):
        return json.dumps({
            'placeName': self.place_name,
            'coordinate': {'latitude': self.latitude,
                           'longitude': self.longitude},
            'size': self.size
        })



if __name__ == '__main__':
    loc = Location('OAMK, Kotkantie campus', 64.99958, 25.51078, 0.00220)
    print(loc)
