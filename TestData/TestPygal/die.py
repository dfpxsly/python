from random import randint

class Die():
	"""docstring for Die"""
	def __init__(self, num_side=6):
		'''默认为6面骰子'''
		self.num_side = num_side

	def roll(self):
		return randint(1,self.num_side)
		