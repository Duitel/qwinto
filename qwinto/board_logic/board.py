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

	def getNumber(y,x):
		return self.arr[y,x]

	def getColumn(col):
		""" returns the values of the column in an array """
		arr1 = self.arr[0:3,col]
		return arr1[arr1 != 0]

	def getRow(row):
		# returns the values of the row in an array
		arr1 = self.arr[row,0:12]
		return arr1[arr1 != 0]

	def isNumberInColumn(num,col):
		for y in getColumn(col):
			if y == num:
				return True
		return False

	def isNumberInRow(num,row):
		for x in getRow(row):
			if x == num:
				return True
		return False

	def isColumnFull(col):
		return getColumn(col).size() == 3

	def isRowFull(row):
		return getRow(row).size() == 9

	def canThisNumberBePlaced(y, x, num):
		return isEmpty(y,x) and !isNumberInColumn(num,x) and !isNumberInRow(num,y)

	def placeNumber(y,x,num):
		if canThisNumberBePlaced(y,x,num):
			self.arr[y,x] = num
			return True
		return False