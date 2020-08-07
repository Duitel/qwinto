from typing import List

from qwinto.game_logic.dice import ChosenDices


class TextGUI:
    def __init__(self):
        self.column_width = 5
        self.row_length = 10
        self.num_rows = 6
        self.build_rows()

    def print_board(self):
        top_border = "+" + "-" * self.row_length * self.column_width + '+'
        middle_rows = []
        for i in range(self.num_rows):
            middle_rows += ["|" + self.make_content_row(i) + "|"]
        print("\n".join([top_border] + middle_rows + [top_border]))

    def make_content_row(self, row_index):
        if row_index == 0:
            return self.build_red()
        elif row_index == 1:
            return self.build_yellow()
        elif row_index == 2:
            return self.build_blue()
        else:
            return self.build_row()

    def pad_text(self, text: str, pad_to_width: int = None, pad_char: str = " ") -> str:
        """Pad a text to the column width.

        :str text: The text to pad.
        :int pad_to_width: The width of the final text
        :str pad_char: The character to pad with
        :returns: the padded text
        """
        if (not pad_to_width):
            pad_to_width = self.column_width

        while (len(text) < pad_to_width):  # Add padding on both sides till length is reached
            text = pad_char + text + pad_char

        if (len(text) > pad_to_width):  # Remove last padding if it was too much
            return text[:-1]
        return text

    def build_rows(self) -> None:
        """Print the red, yellow and blue row."""
        self.build_red()
        self.build_yellow()
        self.build_blue()

    def build_red(self) -> None:
        """Print the red row."""
        return self.build_row(nummber_left_pading_cells=2, empty_cell=3, bonus_cells=[1, 5])

    def build_yellow(self) -> None:
        """Print the yellow row."""
        return self.build_row(nummber_left_pading_cells=1, empty_cell=5, bonus_cells=[7])

    def build_blue(self) -> None:
        """Print the blue row."""
        return self.build_row(nummber_left_pading_cells=0, empty_cell=4, bonus_cells=[2, 9])

    def build_row(self, nummber_left_pading_cells: int = 0, empty_cell: int = -1, bonus_cells: List[int] = []) -> None:
        """Print a row.

        :param left_padding_cells: int, the number of empty cells before the row begins
        :param empty_cell: int, the cell numer to leave empty:
        :returns: None
        """
        row_string = '.' * self.row_length
        if empty_cell >= 0 and empty_cell < len(row_string):
            row_string = row_string[:empty_cell] + " " + row_string[empty_cell + 1:]

        row_string = ''.join(
            self.pad_text(char) if i not in bonus_cells else self.pad_text("{" + char + "}") for i, char in
            enumerate(row_string))

        row_string = ''.join(
            self.pad_text(" ") for _ in range(nummber_left_pading_cells)) + row_string  # Add padding cells on the left

        # Add row
        return row_string

    def startup(self) -> None:
        """Print the introduction to the game."""
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

    def setup_game(self) -> List[str]:
        """Set up the game parameters like the number of players and the name of the players."""
        players = []
        while True:
            number_players = input("How many players will play?  ")
            # convert to integer if inputed a number
            if number_players.isdecimal():
                number_players = int(number_players.strip())
                break  # break out of while
            print("Unallowed input: please input only numbers.")

        # Fill the player positions
        for i in range(number_players):
            players.append(input(f"Who will be playin as player {i}:  "))

        print("\nAll rigth! We are ready to begin:\n")
        return players

    def ask_true_false_question(self, question: str, true_answer: str = "y", false_answer: str = "n",
                                try_again_message: str = None) -> bool:
        """Ask a true or false question from the user. Stop when the answer matches one of the predefined answers.

        :param question: The question to ask the user.
        :type question: str
        :param true_answer: What answer to accept as 'True'
        :type true_answer: str
        :param false_answer: What answer to accept as 'False'
        :type false_answer: str
        :param try_again_message: The message to print when none of the predefined answers is given.
        :type try_again_message: str
        :return: True if the true_answer is given, False if the false_answer is given. Retry otherwise.
        :rtype: bool
        """
        if not try_again_message:
            try_again_message = f"Unallowed input: please respond with '{true_answer}' or '{false_answer}'."
        while True:
            user_input = input(question + f" [{true_answer}/{false_answer}]  ").lower()
            if user_input == true_answer:
                return True
            elif user_input == false_answer:
                return False
            else:
                print(try_again_message)

    def pick_dice(self, color: str) -> bool:
        """Ask the user to include a dice of a specific color or not.

        :param color: The color of the dice.
        :type color: str
        :return: True if the dice is picked, false otherwise.
        :rtype: bool
        """
        return self.ask_true_false_question(question=f"Do you want to roll the {color} dice?")

    def choose_dice(self) -> None:
        """Choose the dice set"""
        while True:
            red = self.pick_dice("red")
            yellow = self.pick_dice("yellow")
            blue = self.pick_dice("blue")
            if red + yellow + blue == 0:
                print("You picked no dice. This is not allowed. Please try again.")
                continue

            print(f"You chose the dices: {'red ' if red else ''}{'yellow ' if yellow else ''}{'blue' if blue else ''}")
            if self.ask_true_false_question(question="Do you want to stick with your choice of dices?"):
                break
