from Functionality.Player import *
from Functionality.Symbol import *
from Functionality.Winner import *
from Exceptions import *

RowCount = 3
ColumnCount = 3

class Board:


    def __init__(self):
        self.reset()

    def reset(self):
        self._lastSelectedField = None
        self._board = [[Player(Symbol.none) for i in range(ColumnCount)] for j in range(RowCount)] #List Comprehensions

    def dropToColumn(self, column, state):
        selectedField = None
        for i in range(RowCount - 1, -1, -1):
            if (self._board[i][column].getSymbol() == Symbol.none):
                selectedField = Player(i, column, state)
                self._board[i][column] = selectedField
                break
        if (selectedField == None):
            raise FullColumnException(column)

        self._lastSelectedField = selectedField

    def isFieldOccupied(self, row, column):
        return self._board[row][column].getSymbol() != Symbol.none

    def getField(self, row, column):
        return self._board[row][column]

    def setField(self, row, column, player):
        self._board[row][column] = player

    def whoHasFinished(self):
        self._winner = Winner(self._board)
        return self._winner.getWinner()




