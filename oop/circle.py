import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        print('__eq__')
        return self.radius == other.radius

    def __str__(self):
        return  f'Radius : {self.radius}'

    def __gt__(self, other):
        return self.radius > other.radius

    def get_area(self):
        return math.pi * self.radius ** 2


c1 = Circle(10)
c2 = Circle(10)
c3 = Circle(30)
print(c1)   # c1.__str__()
# print(id(c1))
# print(id(c2))
print(c1 == c2)  # c1.__eq__(c2)
print(c1 != c2)
print(c1.get_area())

#print(c3 > c2)  # c3.__gt__(c2)

circles = [c1, c2, c3]
sorted(circles)
