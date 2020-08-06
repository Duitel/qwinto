from typing import List


class TextGUI:
	def __init__(self):
		self.column_width = 5
		self.row_length = 10
		self.print_rows()

	def pad_text(self, text:str, pad_to_width:int=None, pad_char:str=" ") -> str:
		"""Pad a text to the column width.

		:str text: The text to pad.
		:int pad_to_width: The width of the final text
		:str pad_char: The character to pad with
		:returns: the padded text
		"""
		if(not pad_to_width):
			pad_to_width = self.column_width

		while(len(text) < pad_to_width): # Add padding on both sides till length is reached
			text = pad_char + text + pad_char

		if(len(text) > pad_to_width): # Remove last padding if it was too much
			return text[:-1] 
		return text

	def print_rows(self) -> None:
		"""Print the red, yellow and blue row."""
		self.print_red()
		self.print_yellow()
		self.print_blue()

	def print_red(self) -> None:
		"""Print the red row."""
		self.print_row(nummber_left_pading_cells=2, empty_cell=3,bonus_cells=[1,5])

	def print_yellow(self) -> None:
		"""Print the yellow row."""
		self.print_row(nummber_left_pading_cells=1, empty_cell=5 ,bonus_cells=[7])

	def print_blue(self) -> None:
		"""Print the blue row."""
		self.print_row(nummber_left_pading_cells=0, empty_cell=4 ,bonus_cells=[2,9])
	
	def print_row(self, nummber_left_pading_cells:int, empty_cell:int, bonus_cells:List[int]) -> None:
		"""Print a row.

		:param left_padding_cells: int, the number of empty cells before the row begins
		:param empty_cell: int, the cell numer to leave empty:
		:returns: None
		"""
		row_string = '.' * self.row_length
		if empty_cell >= 0 and empty_cell < len(row_string):
			row_string = row_string[:empty_cell] + " " + row_string[empty_cell + 1:]

		row_string = ''.join(self.pad_text(char) if i not in bonus_cells else self.pad_text("{"+char+"}") for i,char in enumerate(row_string))

		row_string = ''.join(self.pad_text(" ") for _ in range(nummber_left_pading_cells)) + row_string # Add padding cells on the left
		
		# Add row
		print(row_string)


