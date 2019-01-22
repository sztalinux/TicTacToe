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
        self._rowCount = 3
        self._columnCount = 3
        self._board = Board(self._rowCount, self._columnCount)
        self._winner = Winner(self._board, self._rowCount, self._columnCount)
        self._playerToThrow = self._playerX
        self._boardIsFull = False

    def startGame(self, player):
        if player == 1:
            self._playerToThrow = self._playerX
        elif player == 2:
            self._playerToThrow = self._playerO
        else:
            self._playerToThrow = Player(Symbol.none)
        self._board.reset()

    def getPlayerToThrow(self):
        return self._playerToThrow

    def getWinner(self):
        return self._winner.getWinner()

    def getFieldState(self, row, column):
        return self._board.getField(row, column).getSymbol()

    def getField(self, row, column):
        return self._board.getField(row, column)

    def switchPlayers(self):
        if (self._playerToThrow == self._playerX):
            self._playerToThrow = self._playerO
        else:
            self._playerToThrow = self._playerX

    def whoHasWon(self):
        return self._board.whoHasWon()

    def getPressedField(self, boardX, boardY, fieldH, fieldW, gap):
        if(pygame.mouse.get_pressed()[0] == 1):
            for row in range(self._rowCount):
                for column in range(self._columnCount ):
                    if((boardX + (column + 1) * fieldW > pygame.mouse.get_pos()[0] > boardX + column * fieldW + (column + 1) * gap)
                            and ( boardY + (row + 1) * fieldW > pygame.mouse.get_pos()[1] > boardY + row * fieldH + (row + 1)* gap)
                            and not self._board.isFieldOccupied(row, column)):
                        self._board.setField(row, column, self._playerToThrow)
                        self.switchPlayers()
                        return True
        return False

    def boardIsFull(self):
        for row in range(self._rowCount):
            for column in range(self._columnCount):
                if self.getField(row, column).getSymbol() == Symbol.none:
                    self._boardIsFull = False
                    return self._boardIsFull
        self._boardIsFull = True
        return self._boardIsFull

    def setBoardIsFull(self, param):
        self._boardIsFull = param


    def setField(self, row, column, player):
        self._board.setField(row, column, player)