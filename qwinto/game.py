from qwinto.GUI.TextGUI import TextGUI


class Game:
    def __init__(self):
        self.players = []
        self.active_player = 0
        self.gui = TextGUI()

    def start(self):
        self.gui.startup()
        self.players = self.gui.setup_game()

        while True:
            for player in self.players:
                print(player)
                self.gui.print_board()

            print()
            print(f"{self.players[self.active_player]} it is your turn to roll the dice!")
            self.gui.choose_dice()

            self.active_player += 1
            if self.active_player == len(self.players):
                self.active_player = 0
