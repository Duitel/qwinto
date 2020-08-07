from qwinto.GUI.TextGUI import TextGUI


class Game:
    def __init__(self):
        self.players = []
        self.gui = TextGUI()

    def start(self):
        print("Let's play a game of Qwinto")
        print(
            r"""
              ____ 
             /\' .\    _____ 
            /: \___\  / .  /\ 
            \' / . / /____/..\ 
             \/___/  \'  '\  / 
                      \'__'\/
        """)

        # Set the number of players
        while True:
            number_players = input("How many players will play?")
            # convert to integer if inputed a number
            if number_players.isdecimal():
                self.number_players = int(number_players.strip())
                break  # break out of while
            print("Unallowed input: please input only numbers.")

        # Fill the player positions
        for i in range(self.number_players):
            self.players.append(input(f"Who will be playin as player {i}"))

        for player in self.players:
            print(player)
            self.gui.print_board()
