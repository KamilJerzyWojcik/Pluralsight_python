from abc import ABC, abstractmethod

class UIControl(ABC):
	@abstractmethod
	def draw(self):
		pass


class TextBox(UIControl):
	def draw(self):
		print("text box")


class DropDownList(UIControl):
	def draw(self):
		print("drop down list")


def draw(controls):
	for control in controls:
		control.draw()

ddl = DropDownList()
txt = TextBox()
draw([ddl, txt])