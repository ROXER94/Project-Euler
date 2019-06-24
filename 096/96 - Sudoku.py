# Calculates the sum of the 3-digit numbers found in the top left corner of each sudoku solution grid

from copy import copy

empty = 0

def Sudoku(board):
	if isComplete(board): return board
	r,c = findFirstEmpty(board)
	for i in antiboard[r][c]:
		board[r][c] = i
		if isBoardValid(board):
			result = Sudoku(board)
			if isComplete(board):
				return result
		board[r][c] = empty
	return board

def isComplete(board):
	return all(all(val is not empty for val in row) for row in board)

def findFirstEmpty(board):
	for r,row in enumerate(board):
		for c,val in enumerate(row):
			if val == empty:
				return r,c
	return False

def isBoardValid(board):
	return isRowsValid(board) and isColsValid(board) and isBlocksValid(board)

def isRowsValid(board):
	for row in board:
		if isDuplicates(row):
			return False
	return True

def isColsValid(board):
	for j in range(len(board[0])):
		if isDuplicates([board[i][j] for i in range(len(board))]):
			return False
	return True

def isBlocksValid(board):
	for r in range(0,9,3):
		for c in range(0,9,3):
			block = []
			for a in range(3):
				for b in range(3):
					block.append(board[r+a][c+b])
			if isDuplicates(block):
				return False
	return True

def isDuplicates(array):
	c = {}
	for i in array:
		if i in c.keys() and i is not empty:
			return True
		c[i] = True
	return False

def updateAntiboard(board):
	for thisRowIndex,thisRow in enumerate(board):
		for thisColIndex,thisNumber in enumerate(thisRow):
			if thisNumber is not empty:
				removeRowNumber(thisNumber,thisRowIndex)
				removeColNumber(thisNumber,thisColIndex)
				removeBlockNumber(thisNumber,thisRowIndex,thisColIndex)
				antiboard[thisRowIndex][thisColIndex] = []
	for thisRowIndex,thisRow in enumerate(antiboard):
		for thisColIndex,i in enumerate(thisRow):
			if len(i) == 1:
				board[thisRowIndex][thisColIndex] = i[0]
				antiboard[thisRowIndex][thisColIndex] = []
				updateAntiboard(board)
	return

def removeRowNumber(number,rowIndex):
	for i in range(9):
		if number in antiboard[rowIndex][i]:
			antiboard[rowIndex][i].remove(number)

def removeColNumber(number,colIndex):
	for i in range(9):
		if number in antiboard[i][colIndex]:
			antiboard[i][colIndex].remove(number)

def removeBlockNumber(number,rowIndex,colIndex):
	r,c = 0,0
	while rowIndex - 3 >= 0:
		r += 3
		rowIndex -= 3
	while colIndex - 3 >= 0:
		c += 3
		colIndex -= 3
	for a in range(3):
		for b in range(3):
			if number in antiboard[r+a][c+b]:
				antiboard[r+a][c+b].remove(number)

sudokus = []
with open("sudoku.txt") as file:
	sudoku = []
	for line in file:
		if "Grid" in line:
			if len(sudoku) != 0:
				sudokus.append(sudoku)
			sudoku = []
		else:
			row = [int(i) for i in line.replace("\n","")]
			sudoku.append(row)
	sudokus.append(sudoku)

Sum = 0
for board in sudokus:
	antiboard = [copy([copy([i for i in range(1,10)]) for j in range(1,10)]) for k in range(1,10)]
	updateAntiboard(board)
	Sum += int("".join(str(i) for i in Sudoku(board)[0][0:3]))
print(Sum)
