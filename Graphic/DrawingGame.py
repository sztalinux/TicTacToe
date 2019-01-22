import os

from Functionality.Game import *
from Graphic.Drawing import *
from Graphic.ps import *
class DrawingGame(Window):
    def __init__(self):
        super().__init__()
        self._boardWidth = ColumnCount
        self._boardHeight = RowCount
        self._boardCornerX = 100
        self._boardCornerY = 100
        self._game = Game()
        self._whoseTurnButton = self.createWhoseTurnButton()

    def createWhoseTurnButton(self):
        textColour = colours["BLACK"]
        buttonWidth = 200
        buttonHeight = 50
        buttonX = 300
        buttonY = 150

        # if (whoseTurn == Player1):
        #     whoseTurn = "TURA GRACZA 1"
        #     buttonColour = colours["DARK RED"]
        # elif (whoseTurn == Player2):
        #     whoseTurn = "TURA GRACZA 2"
        #     buttonColour = colours["BRIGHT ORANGE"]
        # else:
        #     whoseTurn = "WCISNIJ START"

        return Button(self._window, buttonX, buttonY, buttonWidth, buttonHeight, colours["GREEN"], ("DUPA", 40, textColour))

    def boardDraw(self):
        board = pygame.image.load('plansza.png')
        self._window.blit(board, (100, 100))

    def drawScreen(self):
        self.boardDraw()


    def setField(self, column):
        try:
            self._game.dropToColumn(column)
        except FieldOccupiedException as full:
            print(full.getMessage())
