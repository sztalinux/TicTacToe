import sys

import pygame as pygame

from Graphic.Drawing import *
from Graphic.DrawingMenu import *
from Graphic.DrawingGame import *
from Graphic.DrawingSignSelection import *
from Graphic.Window import *


class mainLoop:
    def __init__(self):
        self._game = Game()
        self._menuWindow = DrawingMenu(self._game)
        self._gameWindow = DrawingGame(self._game)
        self._signSelectionWindow = DrawingSignSelection(self._game)
        self._started = True


    def loop(self):

        while not self._menuWindow.ifEndClicked:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            if not self._menuWindow.ifStartClicked:
                self._menuWindow.drawScreen()
                self._signSelectionWindow.setIfMenuClicked(False)
            elif self._menuWindow.ifStartClicked:
                self._menuWindow.clear()
                self._signSelectionWindow.drawScreen()
                if self._signSelectionWindow.ifMenuClicked:
                    self._menuWindow.clear()
                    self._menuWindow.setIfStartClicked(False)
                elif self._signSelectionWindow.ifPlayClicked:
                    self._menuWindow.clear()
                    if not self._started:
                        self._signSelectionWindow.startTheGame()
                        self._started = True
                    self.start()


            # self._menuWindow.clear()
            pygame.display.flip()

    def start(self):

        self._gameWindow.drawScreen()
        while (True):
            self._gameWindow.drawScreen()
            winner = self._game.whoHasWon()
            if winner != Symbol.none or self._game.boardIsFull():
                self._gameWindow.drawWinner(winner)
                break
            elif self._gameWindow.ifResetClicked:
                self._started = False
                self._gameWindow.setIfResetClicked(False)
                self._game.setBoardIsFull(False)
                winner = Symbol.none
                break
            elif self._gameWindow.ifMenuClicked:
                self._started = False
                self._menuWindow.clear()
                self._menuWindow.setIfStartClicked(False)
                self._signSelectionWindow.setIfPlayClicked(False)
                self._signSelectionWindow.setIfMenuClicked(False)
                break
            else:
                self._gameWindow.wasMoved()
                break






