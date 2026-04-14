class Counter:
    # Constructor
    def __init__(self, start=0):
        # Object Attributes
        self.value = start

    # Methods
    def inc(self, step=1):
        self.value += step

    def dec(self):
        self.value -= 1

    def get_value(self):
        return self.value

    @property
    def currentvalue(self):
        return self.value


c1 = Counter()  # Object
print(c1.currentvalue)  # Property
c1.inc()
c1.inc(5)
print(c1.currentvalue)

c2 = Counter(100)  # Object
print(c2.currentvalue)
