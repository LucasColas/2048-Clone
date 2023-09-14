import numpy as np
import pygame

class Board:
    def __init__(self, size_board : int, screen : pygame.Surface):
        self.screen = screen
        self.size_board = size_board
        self.board_values = np.zeros((self.size_board, self.size_board))
        self.cell_colors = {
            2 : (238, 228, 218),
            4 : (237, 224, 200),
            8 : (242, 177, 121),
            16 : (245, 149, 99),
            32 : (246, 124, 96),
            64 : (246, 94, 59),
            128 : (237, 207, 115),
            256 : (237, 204, 98),
            512 : (237, 200, 80),
            1024 : (237, 197, 63),
            2048 : (237, 194, 45),
        }

    def draw_board(self, screen : pygame.Surface):
        pass



    