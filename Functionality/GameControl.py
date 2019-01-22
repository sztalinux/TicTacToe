
from Graphic.DrawingGame import *
from Graphic.DrawingSignSelection import *

class GameControl():
    def __init__(self, signSelectionWindow, gameWindow):
        self._gameWindow = gameWindow
        self._signSelectionWindow = signSelectionWindow
        self._game = Game()

    def start(self):
        self._signSelectionWindow.startTheGame()
        self._gameWindow.drawScreen()
        # while(self._game.whoHasWon() == Symbol.none):
        #     pass
