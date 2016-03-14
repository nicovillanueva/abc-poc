import abc

class BaseAttack(abc.ABC):

	def __init__(self, p):
		self.p = p
		print("My name is {} and I'm being set up with parameter: {}".format(self.__class__.__name__, p))

	@abc.abstractmethod
	def run(self):
		pass

	@abc.abstractmethod
	def check(self):
		pass

	@abc.abstractmethod
	def setup(self):
		pass
