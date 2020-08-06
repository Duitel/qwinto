from qwinto.game_logic.dice import ChosenDices


def main():
	print("Hello world!")

	print("Throwing the red and the yellow dices")
	dice_set = ChosenDices(red=True, yellow=True)
	for i in range(10):
		print("Throw:", dice_set.number_times_thrown, "Thrown: ", dice_set.throw_dices())

if __name__ == '__main__':
  main()