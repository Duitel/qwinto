from random import randint


class ChosenDices:
	def __init__(self, red:bool=False, yellow:bool=False, blue:bool=False):
		red_dice = red
		yellow_dice = yellow
		blue_dice = blue
		self.number_of_dices = red + yellow + blue
		self.number_times_thrown = 0

	def throw_dices(self):
		"""Throw the selected dices and return the sum of the dices.

		:returns: int, the sum of the dice.
		"""
		self.number_times_thrown += 1
		return sum(randint(1,6) for _ in range(self.number_of_dices))
