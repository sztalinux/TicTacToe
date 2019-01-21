import pygame
from Graphic.Drawing import *
from Functionality.Board import *
from Functionality.Player import *
from Functionality.Symbol import *
from Functionality.Winner import *


class Game():
    def __init__(self):
        self._playerX = Player(Symbol.X)
        self._playerO = Player(Symbol.O)
        self._board = Board()
        self._winner = Winner(self._board)
        self._playerToThrow = self._playerX

    def startGame(self, player):
        if player == 1:
            self._playerToThrow = self._playerX
        elif player == 2:
            self._playerToThrow = self._playerY
        else:
            self._playerToThrow = Player(Symbol.none)
        self._board.reset()

    def getPlayerToThrow(self):
        return self._playerToThrow

    def getWinner(self):
        return self._winner.getWinner()

    def getFieldState(self, row, column):
        return self._board.getField(row, column).getSymbol()

    def dropToColumn(self, column):
        self._board.dropToColumn(column, self._playerToThrow)
        self.switchPlayers()

    def getField(self, row, column):
        return self._board.getField(row, column)

    def isColumnFull(self, column):
        return self._board.getField(0, column).getSymbol() != Empty

    def switchPlayers(self):
        if (self._playerToThrow == Player1):
            self._playerToThrow = Player2
        else:
            self._playerToThrow = Player1
