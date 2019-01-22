import pygame
from Graphic.Colours import *

class Window:
    def __init__(self):
        pygame.init()
        self._windowWidth = 1280
        self._windowHeight = 720
        self._name = 'TicTacToe'
        self._window = pygame.display.set_mode((self._windowWidth, self._windowHeight))
        pygame.display.set_caption(self._name)
        self.fillBackground()
        #pygame.display.toggle_fullscreen

    def fillBackground(self):
        self._window.fill((colours["WHITE"]))

    @property
    def getWindow(self):
        return self._window