from Button import *
from Functionality.Board import *
from Functionality.Game import *


class Drawing(Window):
    def __init__(self):
        super().__init__()
        self._textColour = colours["BLACK"]
        self._buttonColour = colours["GRAY"]
        self._buttonWidth = 100
        self._buttonHeight = 50


    def setButtonsState(self, enabled):
        for i in range(ColumnCount):
            self._buttons[i].setEnabled(enabled)


    def checkWinner(self):
        winner = self._game.getWinner()
        lastWinner = self.createWinnerButton(winner)
        if (winner != Empty):
            lastWinner.draw()
            self.setButtonsState(False)
        columnFull = 0
        for column in range(ColumnCount):
            if (winner == Empty and self._game.isColumnFull(column)):
                columnFull += 1
        if (winner == Empty and columnFull == 7):
            lastWinner.draw()
            self.setButtonsState(False)




