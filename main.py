import pygame
import numpy as np
import sys

from Game.Board import Board
from Game.game import Game

pygame.init()


def main():
    board_size = 4
    shift = 150

    # screen resolution
    resolution = (570, 720)
    screen = pygame.display.set_mode(resolution)
    # board = Board(board_size, board_size, board_size, shift, screen)
    game = Game(screen, board_size, shift, screen.get_width(), screen.get_height())
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Exit the program when the window is closed

        game.update_window()


if __name__ == "__main__":
    main()
