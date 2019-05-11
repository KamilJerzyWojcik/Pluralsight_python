class Employee:
	def greet(self):
		print("Employee greet")


class Person:
	def greet(self):
		print("Person gteet")


class Manager(Employee, Person):
	pass

m = Manager()
m.greet()


class Flyer:
	def fly(self):
		pass


class Swimmer:
	def swim(self):
		pass


class FlayerFish(Flyer, Swimmer):
	pass

