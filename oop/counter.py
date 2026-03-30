class Counter:
    # Constructor
    def __init__(self):
        # Object Attributes
        self.value = 0

    # Methods
    def inc(self):
        self.value += 1

    def dec(self):
        self.value -= 1

    def get_value(self):
        return self.value

c1 = Counter()   # Object
print(c1.get_value())
c1.inc()
c1.inc()
print(c1.get_value())

c2 = Counter()   # Object
print(c1.get_value())
