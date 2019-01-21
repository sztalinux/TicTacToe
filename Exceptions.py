from Graphic.Colours import *



class FieldOccupiedException(Exception):
    def __init__(self, column):
        self._message = "Cannot throw to column {} because it is full".format(column + 1)

    def getMessage(self):
        return self._message