from random import randint

class Dice:
	def __init__(color: str):
		this.color = color

	def throw() -> int:
		"""Throw the dice.

		:returns: int, a random number between 1 and 6
		"""
		return randint(1,6)
