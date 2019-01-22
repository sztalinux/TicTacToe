from Functionality.Player import *
from Functionality.Symbol import *
from Functionality.Winner import *
from Functionality.Winner import Winner

RowCount = 3
ColumnCount = 3

class Board:


    def __init__(self, row, column):
        self.reset()
        self._rowCount = row
        self._columnCount = column

    def reset(self):
        self._board = [[Player(Symbol.none) for i in range(ColumnCount)] for j in range(RowCount)] #List Comprehensions


    def isFieldOccupied(self, row, column):
        return self._board[row][column].getSymbol() != Symbol.none

    def getField(self, row, column):
        return self._board[row][column]

    def setField(self, row, column, player):
        self._board[row][column] = player

    def whoHasWon(self):
        self._winner = Winner(self._board, self._rowCount, self._columnCount)
        return self._winner.getWinner()




