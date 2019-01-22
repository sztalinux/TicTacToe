from Functionality.Game import *

from Graphic.Drawing import *

class DrawingSignSelection(Window):
    def __init__(self, game):
        super().__init__()
        self._player = 0
        self._game = game
        self._ifPlayClicked = False
        self._ifMenuClicked = False
        self._playButton = self.createPlayButton()
        self._menuButton = self.createMenuButton()
        self._XButton = self.createXButton()
        self._OButton = self.createOButton()
        self._playButton.setEnabled(False)

    def createXButton(self):
        textColour = colours["BLACK"]
        buttonWidth = 200
        buttonHeight = 50
        buttonX = 50
        buttonY = 0
        clickAction = lambda: self.setXPlayer()  # lambda
        return Button(self._window, buttonX, buttonY, buttonWidth, buttonHeight, colours["GRAY"], colours["DARK GRAY"], ("X", 40, textColour), clickAction)

    def createOButton(self):
        textColour = colours["BLACK"]
        buttonWidth = 200
        buttonHeight = 50
        buttonX = 300
        buttonY = 0
        clickAction = lambda: self.setOPlayer()  # lambda
        return Button(self._window, buttonX, buttonY, buttonWidth, buttonHeight, colours["GRAY"], colours["DARK GRAY"], ("O", 40, textColour), clickAction)

    def createPlayButton(self):
        textColour = colours["BLACK"]
        buttonWidth = 200
        buttonHeight = 50
        buttonX = 50
        buttonY = 100
        clickAction = lambda: self.startTheGame()  # lambda
        return Button(self._window, buttonX, buttonY, buttonWidth, buttonHeight, colours["GRAY"], colours["DARK GRAY"], ("PLAY", 40, textColour), clickAction)

    def createMenuButton(self):
        textColour = colours["BLACK"]
        buttonWidth = 200
        buttonHeight = 50
        buttonX = 300
        buttonY = 100
        clickAction = lambda: self.backToMenu()  # lambda
        return Button(self._window, buttonX, buttonY, buttonWidth, buttonHeight, colours["GRAY"], colours["DARK GRAY"], ("MENU", 40, textColour), clickAction)

    def drawScreen(self):
        self._playButton.draw()
        self._menuButton.draw()
        self._XButton.draw()
        self._OButton.draw()

    def setXPlayer(self):
        # rysowanie sie otoczki nad tym
        self._playButton.setEnabled(True)
        self._XButton.setEnabled(False)
        self._OButton.setEnabled(True)
        self._player = 1

    def setOPlayer(self):
        # rysowanie sie otoczki nad tym
        self._playButton.setEnabled(True)
        self._OButton.setEnabled(False)
        self._XButton.setEnabled(True)
        self._player = 2

    def startTheGame(self):
        self._game.startGame(self._player)
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

    def setIfPlayClicked(self, param):
        self._ifPlayClicked = param


