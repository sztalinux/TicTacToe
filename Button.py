from Graphic.Window import *

class Button():
    def __init__(self, window, x, y, width, height, normalColour, highlightedColour, text=("", 0, 0), action=None):
        self._window = window
        self._x = x
        self._y = y
        self._w = width
        self._h = height
        self._ic = normalColour
        self._ac = highlightedColour
        self._action = action
        self._text, self._textSize, self._textColour = text
        self._wasClicked = False
        self._enabled = True

    def isMouseOver(self):
        mouse = pygame.mouse.get_pos()
        return self._x + self._w > mouse[0] > self._x and self._y + self._h > mouse[1] > self._y

    def draw(self):
        if not self._enabled:
            self._ac = self._ic
        if self._enabled and self.isMouseOver():
            self.drawHighlighted()
            click = pygame.mouse.get_pressed()
            if(click[0] == 1):
                self._wasClicked = True
            elif(self._wasClicked):
                self._action()
                self._wasClicked = False
        else:
            self.drawNormal()
            self._wasClicked = False
        self.drawText()


    def drawNormal(self):
        pygame.draw.rect(self._window, self._ic, (self._x, self._y, self._w, self._h))

    def drawHighlighted(self):
        pygame.draw.rect(self._window, self._ac, (self._x, self._y, self._w, self._h))

    def drawText(self):
        myFont = pygame.font.SysFont("freesansbold.ttf", self._textSize)
        text = myFont.render(self._text, 1, self._textColour)
        self._window.blit(text, (self._x + ((self._w - text.get_rect().width) / 2), self._y + ((self._h - text.get_rect().height) / 2)))

    def setEnabled(self, enabled):
        self._enabled = enabled