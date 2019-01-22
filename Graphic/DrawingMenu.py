from Functionality.Game import *
from Graphic.Drawing import *


class DrawingMenu(Window):
    def __init__(self):
        super().__init__()
        self._game = Game()
        self._ifStartClicked = False
        self._ifEndClicked = False
        self._startButton = self.createStartButton()
        self._endButton = self.createEndButton()

    def createStartButton(self):
        textColour = colours["BLACK"]
        buttonWidth = 200
        buttonHeight = 50
        buttonX = 50
        buttonY = 50
        clickAction = lambda: self.startTheGame()  # lambda
        return Button(self._window, buttonX, buttonY, buttonWidth, buttonHeight, colours["GRAY"], ("START", 40, textColour), clickAction)

    def createEndButton(self):
        textColour = colours["BLACK"]
        buttonWidth = 200
        buttonHeight = 50
        buttonX = 300
        buttonY = 50
        clickAction = lambda: self.endTheGame()  # lambda
        return Button(self._window, buttonX, buttonY, buttonWidth, buttonHeight, colours["GRAY"], ("END", 40, textColour), clickAction)

    def drawScreen(self):
        self._startButton.draw()
        self._endButton.draw()

    def startTheGame(self):
        self._ifStartClicked = True

    def endTheGame(self):
        self._ifEndClicked = True

    def clear(self):
        super().fillBackground()


    @property
    def ifStartClicked(self):
        return self._ifStartClicked

    @property
    def ifEndClicked(self):
        return self._ifEndClicked

    def setIfStartClicked(self, param):
        self._ifStartClicked = param

    def setIfEndClicked(self, param):
        self._ifEndClicked = param

    @property
    def endButton(self):
        return self._endButton

    @property
    def startButton(self):
        return self._startButton


