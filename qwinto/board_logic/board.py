import numpy as np

class Board:
	def __init__(self):
		self.arr = np.zeros(3,12)
		""" layout array 
			1 = not part of the board
			-1 = the pentagon symbol on board, the bonus points for a full column"""
		self.layout = np.array([[1,1,0,-1,0,1,0,-1,0,0,0,0],[1,0,0,0,0,0,1,0,-1,0,0,1],[0,0,-1,0,1,0,0,0,0,-1,1,1]])

	def isEmpty(y,x):
		""" Check if spot on the board is avaible & empty"""
		return self.layout[y,x] <= 1 and self.arr[y,x] == 0

	def getColumn(col):
		""" returns the values of the column in an array """
		a=b=c=0
		if self.layout[0,col] != 1:
			

		return self.arr[0:3,col]

	def getRow(row):
		# returns the values of the row in an array
		return self.arr[row,0:12]

	def isNumberInColumn(num,col):
		for x in getColumn(col):
			if x == num:
				return True
		return False

	def isNumberInRow(num,row):
