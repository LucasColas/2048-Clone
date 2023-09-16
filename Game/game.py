import pygame
import numpy as np

from Game.Board import Board
from Game.TopBar import TopBar

pygame.init()

class Game:
    def __init__(self, screen : pygame.Surface, board_size : int, shift : int, width : int, height : int):
        self.board_size = board_size
        self.shift = shift
        self.width = width
        self.height = height
        self.screen = screen
        self.board_width = self.width 
        self.board_height = self.height - shift
        self.board = Board(self.board_size, self.board_width, self.board_height, self.shift, self.screen)
        self.top_bar = TopBar(self.screen)

    def update_window(self):
        self.board.draw_board()
        #self.top_bar.draw_top_bar()
        pygame.display.update()

    