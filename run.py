from qwinto.game_logic.dice import ChosenDices
from qwinto.GUI.TextGUI import TextGUI
from qwinto.game import Game

def main():
	print("Hello world!")

	print("Throwing the red and the yellow dices")
	dice_set = ChosenDices(red=True, yellow=True)
	for i in range(10):
		print("Throw:", dice_set.number_times_thrown, "Thrown: ", dice_set.throw_dices())

	print()
	print("testing GUI")
	textGUI = TextGUI()

	# Testing game
	print()
	print("Testing game")
	game = Game()
	game.start()


if __name__ == '__main__':
  main()