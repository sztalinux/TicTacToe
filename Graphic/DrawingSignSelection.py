from Functionality.Game import *
from Graphic.Drawing import *

class DrawingSignSelection(Window):
    def __init__(self):
        super().__init__()
        self._game = Game()
        self._ifPlayClicked = False
        self._ifMenuClicked = False
        self._playButton = self.createPlayButton()
        self._menuButton = self.createMenuButton()

    def createPlayButton(self):
        textColour = colours["BLACK"]
        buttonWidth = 200
        buttonHeight = 50
        buttonX = 50
        buttonY = 50
        clickAction = lambda: self.startTheGame()  # lambda
        return Button(self._window, buttonX, buttonY, buttonWidth, buttonHeight, colours["GREEN"], ("PLAY", 40, textColour), clickAction)

    def createMenuButton(self):
        textColour = colours["BLACK"]
        buttonWidth = 200
        buttonHeight = 50
        buttonX = 300
        buttonY = 50
        clickAction = lambda: self.backToMenu()  # lambda
        return Button(self._window, buttonX, buttonY, buttonWidth, buttonHeight, colours["GREEN"], ("MENU", 40, textColour), clickAction)

    def startTheGame(self):
        self._game.startGame(Player1)
        self._ifPlayClicked = True

    def backToMenu(self):
        self._ifMenuClicked = True

    def setPlayButtonState(self, enabled):
        self._playButton.setEnabled(enabled)


    @property
    def ifPlayClicked(self):
        return self._ifPlayClicked

    @property
    def ifMenuClicked(self):
        return self._ifMenuClicked

    @property
    def playButton(self):
        return self._playButton

    @property
    def menuButton(self):
        return self._menuButton

    def setIfMenuClicked(self, param):
        self._ifMenuClicked = param
