import os

from Functionality.Game import *
from Graphic.Drawing import *
from Graphic.ps import *
class DrawingGame(Window):
    def __init__(self, game):
        super().__init__()
        self._gap = 20
        self._fieldWidth = 170
        self._fieldHeight = 170
        self._boardCornerX = 350
        self._boardCornerY = 100
        self._fieldX = self._boardCornerX + self._gap
        self._fieldY = self._boardCornerY + self._gap
        self._game = game
        self._XSign = pygame.image.load('X.png')
        self._OSign = pygame.image.load('O.png')
        self._resetButton = self.createResetButton()
        self._menuButton = self.createMenuButton()
        self._ifResetClicked = False
        self._ifMenuClicked = False

    def createResetButton(self):
        textColour = colours["BLACK"]
        buttonWidth = 150
        buttonHeight = 37
        buttonX = 50
        buttonY = 500
        clickAction = lambda: self.reset()  # lambda

        return Button(self._window, buttonX, buttonY, buttonWidth, buttonHeight, colours["GRAY"], colours["DARK GRAY"], ("RESET", 40, textColour), clickAction)

    def createMenuButton(self):
        textColour = colours["BLACK"]
        buttonWidth = 150
        buttonHeight = 37
        buttonX = 50
        buttonY = 600
        clickAction = lambda: self.backToMenu()  # lambda

        return Button(self._window, buttonX, buttonY, buttonWidth, buttonHeight, colours["GRAY"], colours["DARK GRAY"], ("MENU", 40, textColour), clickAction)

    def wasMoved(self):
        moved = self._game.getPressedField(self._boardCornerX, self._boardCornerY, self._fieldHeight, self._fieldWidth, self._gap)


    def updateBoard(self):
        for row in range(0, 3):
            for column in range(0, 3):
                field = self._game.getField(row, column)
                if field.getSymbol() == Symbol.X:
                    self._window.blit(self._XSign, (self._boardCornerX + self._fieldWidth * column + (column + 1) * self._gap, self._boardCornerY + self._fieldHeight * row + (row + 1) * self._gap))
                elif field.getSymbol() == Symbol.O:
                    self._window.blit(self._OSign, (self._boardCornerX + self._fieldWidth * column + (column + 1) * self._gap, self._boardCornerY + self._fieldHeight * row + (row + 1) * self._gap))


    def boardDraw(self):
        board = pygame.image.load('plansza.png')
        self._window.blit(board, (self._boardCornerX, self._boardCornerY))

    def drawScreen(self):
        self.boardDraw()
        self._resetButton.draw()
        self._menuButton.draw()
        self.updateBoard()


    def drawWinner(self, symbol):
        if symbol == Symbol.X:
            board = pygame.image.load('wygranaX.png')
        elif symbol == Symbol.O:
            board = pygame.image.load('wygranaO.png')
        elif symbol == Symbol.none:
            board = pygame.image.load('remis.png')
            self._window.blit(board, (0, 0))

    def reset(self):
        self._ifResetClicked = True
        self._game._board = [[Player(Symbol.none) for i in range(3)] for j in range(3)]

    def backToMenu(self):
        self._ifMenuClicked = True

    def setField(self, column):
        try:
            self._game.dropToColumn(column)
        except FieldOccupiedException as full:
            print(full.getMessage())

    @property
    def ifResetClicked(self):
        return self._ifResetClicked

    @property
    def ifMenuClicked(self):
        return self._ifMenuClicked

