from src.attacks.atk_base import BaseAttack

class Attacker2(BaseAttack):
	def __init__(self, p):
		pass

	def run(self):
		print("Running {}".format(self.__class__.__name__))

	def setup(self):
		print("Setting up {}".format(self.__class__.__name__))

	def check(self):
		print("Checking up {}".format(self.__class__.__name__))
