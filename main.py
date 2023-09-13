import pygame 
import numpy as np
import sys
pygame.init()

def update_window():
    pass


def main():
    Size_board = 4
    Board_values = np.zeros((Size_board, Size_board))

    # screen resolution
    res = (720, 720)
    screen = pygame.display.set_mode(res)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Exit the program when the window is closed


if __name__ == "__main__":
    main()