class Animal:
	def __init__(self):
		self.age = 1
		print("Animal")

	def eat(self):
		print("eat")


class Mammal(Animal):

	def __init__(self):
		super().__init__()
		print("mammal")
		self.weight = 2

	def walk(self):
		print("walk")


class Fish(Animal):
	def swim(self):
		print("swim")

class Bird(Animal):
	def fly(self):
		print("fly")


b = Bird()


f = Fish()
print(isinstance(f, Fish))
print(issubclass(Fish, Animal))


o = object()
