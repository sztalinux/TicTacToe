import sys

import pygame as pygame

from Graphic.Drawing import *
from Graphic.DrawingMenu import *
from Graphic.DrawingGame import *
from Graphic.DrawingSignSelection import *
from Graphic.Window import *
from Functionality.GameControl import *


class mainLoop:
    def __init__(self):
        self._menuWindow = DrawingMenu()
        self._gameWindow = DrawingGame()
        self._signSelectionWindow = DrawingSignSelection()
        self._gameControl = GameControl(self._signSelectionWindow, self._gameWindow)

    def loop(self):

        while not self._menuWindow.ifEndClicked:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            if not (self._menuWindow.ifStartClicked or self._menuWindow.ifEndClicked):
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
                    self._gameWindow.drawScreen()
                    self._gameControl.start()


            # self._menuWindow.clear()
            pygame.display.flip()

