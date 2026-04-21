
import json

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email


p1 = Person("Van Rossum", "rossum@microsoft.com")
print(json.dumps(p1.__dict__))
