import hashlib
import json

class Account:

    def __init__(self, name, login):
        self.name = name
        self.login = login
        self._password = None

    def _set_password(self, value):
        self._password = hashlib.sha3_512(value.encode()).hexdigest()

    password = property(None, _set_password)


    def check_password(self, value):
        return hashlib.sha3_512(value.encode()).hexdigest() == self._password
