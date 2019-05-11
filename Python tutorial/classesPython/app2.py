class TagCloud:
	def __init__(self):
		self.tags = {}

	def add(self, tag):
		self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

	def __getitem__(self, key):
		return self.tags.get(key, 0)

	def __setitem__(self, tag, count):
		self.tags[tag.lower()] = count

	def __len__(self):
		return len(self.tags)

	def __iter__(self):
		return iter(self.tags)



cloud = TagCloud()
cloud.add("python")
print(cloud["python"])
print(cloud["python2"])

cloud.add("python")
cloud.add("Python")
cloud.add("python2")

cloud["python"] = 10

print(len(cloud))

for tag in cloud:
	print(tag)