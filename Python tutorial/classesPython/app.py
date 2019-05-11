class Point:
	default_color = "red"

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return f"{self.x}, {self.y}"

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __gt__(self, other):
		return self.x > other.x and self.y > other.y

	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)

	@classmethod
	def zero(cls):
		return cls(0, 0)


	def draw(self):
		print(f"Point ({self.x}), ({self.y})")

point1 = Point(1,2)
point2 = Point(1,2)
point3 = Point(3,4)
point4 = point1 + point3

print(point4.y)