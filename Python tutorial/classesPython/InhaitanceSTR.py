class Text(str):
	def duplicate(self):
		print(self + self)


class TrackableList(list):
	def append(self, object):
		print("append to list")
		super().append(object)

text = Text("PYTHON")

print(text.lower())
text.duplicate()

l = TrackableList()
l.append(9)