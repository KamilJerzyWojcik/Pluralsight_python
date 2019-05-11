from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
	pass


class Stream(ABC):
	def __init__(self):
		self.opened = False

	def open(self):
		if self.opened:
			raise InvalidOperationError("Stream is already open")
		self.opened = True

	def close(self):
		if self.opened:
			raise InvalidOperationError("Stream is already close")
		self.opened = False

	@abstractmethod
	def read(self):
		pass


class FileStream:

	def read(self):
		print("read data from a file")


class NetworkStream:

	def read(self):
		print("read data from a network")


class MemoryStream(Stream):
	def read(self):
		print("readind data from memory stream")


stream = MemoryStream()

stream.open()