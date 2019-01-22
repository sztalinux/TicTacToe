import pygame
from Graphic.Colours import *
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
class Window:
    def __init__(self):
        pygame.init()
        self._name = 'TicTacToe'
        self._window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(self._name)
        self.fillBackground()
        # pygame.display.toggle_fullscreen()

    def fillBackground(self):
        self._window.fill((colours["WHITE"]))

    @property
    def getWindow(self):
        return self._window