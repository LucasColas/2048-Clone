import pygame
import numpy as np
import sys

#from Game.Board import Board
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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and game.start and not game.board.game_over:
                    game.board.move_left()
                if event.key == pygame.K_RIGHT and game.start and not game.board.game_over:
                    game.board.move_right()
                if event.key == pygame.K_UP and game.start and not game.board.game_over:
                    game.board.move_up()
                if event.key == pygame.K_DOWN and game.start and not game.board.game_over:
                    game.board.move_down()

                # Start game with
                if event.key == pygame.K_SPACE and not game.start:
                    game.start_game()

                

        game.update_window()


if __name__ == "__main__":
    main()
