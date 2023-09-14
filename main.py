import pygame 
import numpy as np
import sys

from Game.Board import Board

pygame.init()

def update_window():
    pass


def main():
    board_size = 4
    

    # screen resolution
    res = (720, 720)
    screen = pygame.display.set_mode(res)
    board = Board(board_size, screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Exit the program when the window is closed


if __name__ == "__main__":
    main()