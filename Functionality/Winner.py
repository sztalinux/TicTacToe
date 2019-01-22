from Functionality.Player import *
from Functionality.Symbol import *
from Functionality.Board import *

class Winner:
    def __init__(self, board):
        self._board = board

    def getFieldState(self, row, column):
        return self._board.getField(row, column).getSymbol()

    def getWinner(self):
        winner = Symbol.none
        rows = self.isFinishedRows()
        columns = self.isFinishedColumns()
        axis1 = self.isFinishedAxis1()
        axis2 = self.isFinishedAxis2()
        if rows != Symbol.none:
            winner = rows
        elif columns != Symbol.none:
            winner = columns
        elif axis1 != Symbol.none:
            winner = axis1
        elif axis2 != Symbol.none:
            winner = axis2
        return winner

    def isFinishedRows(self):
        for row in range(0, RowCount - 1, 1):
            countX = 0
            countO = 0

            for column in range(0, ColumnCount - 1, 1):
                if self._board[row][column].getSymbol() == Symbol.X:
                    countX = countX + 1
                elif self._board[row][column].getSymbol() == Symbol.O:
                    countO = countO + 1
                else:
                    continue

            if countX == RowCount:
                return Symbol.X
            elif countO == ColumnCount:
                return Symbol.Y

        return Symbol.none

    def isFinishedColumns(self):
        for column in range(0, ColumnCount - 1, 1):
            countX = 0
            countO = 0

            for row in range(0, RowCount - 1, 1):
                if self._board[row][column].getSymbol() == Symbol.X:
                    countX = countX + 1
                elif self._board[row][column].getSymbol() == Symbol.O:
                    countO = countO + 1
                else:
                    continue

            if countX == RowCount:
                return Symbol.X
            elif countO == ColumnCount:
                return Symbol.Y

        return Symbol.none

    def isFinishedAxis1(self):
        countX = 0
        countO = 0
        for row in range(0, RowCount - 1, 1):
            column = row
            if self._board[row][column].getSymbol() == Symbol.X:
                countX = countX + 1
            elif self._board[row][column].getSymbol() == Symbol.O:
                countO = countO + 1
            else:
                continue

            if countX == RowCount:
                return Symbol.X
            elif countO == ColumnCount:
                return Symbol.Y

        return Symbol.none


    def isFinishedAxis2(self):
        countX = 0
        countO = 0
        for row in range(0, RowCount - 1, 1):
            column = RowCount - 1 - row
            if self._board[row][column].getSymbol() == Symbol.X:
                countX = countX + 1
            elif self._board[row][column].getSymbol() == Symbol.O:
                countO = countO + 1
            else:
                continue

            if countX == RowCount:
                return Symbol.X
            elif countO == ColumnCount:
                return Symbol.Y

        return Symbol.none