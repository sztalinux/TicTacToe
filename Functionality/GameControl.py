
from Graphic.DrawingGame import *
from Graphic.DrawingSignSelection import *

class GameControl():
    def __init__(self, signSelectionWindow, gameWindow):
        self._gameWindow = gameWindow
        self._signSelectionWindow = signSelectionWindow

    def start(self):
        self._signSelectionWindow.startTheGame()
