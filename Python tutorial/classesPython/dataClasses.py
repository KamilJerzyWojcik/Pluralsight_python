from collections import namedtuple

PointTuple = namedtuple("PointTuple", ["x", "y"])

p3 = PointTuple(x=1, y=2)
p4 = PointTuple(x=1, y=2)
print(p3.x)
#p3.x = 10
print(p3 == p4)

class Point():
    def greetGre(self):
        print("hello point")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x


p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2)

print(id(p1))
print(id(p2))