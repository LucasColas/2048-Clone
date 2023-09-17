import numpy as np
import pygame


class Board:
    def __init__(
        self,
        board_size: int,
        board_width: int,
        board_height: int,
        shift: int,
        screen: pygame.Surface,
    ):
        self.screen = screen
        self.board_size = board_size
        self.board_width = board_width
        self.board_height = board_height
        # print("board_width: ", self.board_width, "board_height: ", self.board_height)
        self.shift = shift
        self.padding = 0.02 * self.board_width
        self.nb_padding = self.board_size + 1
        # print("padding: ", self.padding)
        self.board_values = np.zeros((self.board_size, self.board_size), dtype=int)
        self.cell_colors = {
            0: (205, 193, 180),
            2: (238, 228, 218),
            4: (237, 224, 200),
            8: (242, 177, 121),
            16: (245, 149, 99),
            32: (246, 124, 96),
            64: (246, 94, 59),
            128: (237, 207, 115),
            256: (237, 204, 98),
            512: (237, 200, 80),
            1024: (237, 197, 63),
            2048: (237, 194, 45),
        }
        self.text_color = (119, 110, 101)
        self.blank_color = (184, 174, 161)
        self.cell_rects = self.create_cell_rects()

    def create_Rect(self, row: int, col: int):
        cell_width = (
            self.board_width - self.nb_padding * self.padding
        ) // self.board_size
        cell_height = (
            self.board_height - self.nb_padding * self.padding
        ) // self.board_size

        x = col * cell_width + (col + 1) * self.padding
        y = row * cell_height + (row + 1) * self.padding + self.shift
        # print("x: ", x, "y: ", y, "cell_width: ", cell_width, "cell_height: ", cell_height)
        return pygame.Rect(x, y, cell_width, cell_height)
    
    def generate_random_value_for_cell(self):
        empty_cells = np.argwhere(self.board_values == 0)
        if len(empty_cells) == 0:
            return
        random_cell = empty_cells[np.random.randint(0, len(empty_cells))]
        self.board_values[random_cell[0], random_cell[1]] = 2

    def create_cell_rects(self):
        cell_rects = np.zeros((self.board_size, self.board_size), dtype=pygame.Rect)
        for row in range(self.board_size):
            for col in range(self.board_size):
                cell_rects[row, col] = self.create_Rect(row, col)

        return cell_rects

    def move_up(self):
        """
        
        Move every value to the top of the board.
        Stop moving when there's a value or the end of the board.
        If there's a value, check if it's equal to the current value.
        If it is, merge them.
        
        """

        for col in range(self.board_size):
            for row in range(self.board_size):
                # Shift up each value until we hit a value or the end of the board
                if self.board_values[row, col] == 0:
                    continue
                current_val = self.board_values[row, col]
                current_row = row
                while current_row > 0 and self.board_values[current_row-1, col] == 0:
                    current_row -= 1
                if current_row != row:
                    self.board_values[current_row, col] = current_val
                    self.board_values[row, col] = 0
        
        # Merge values if they're equal

        for col in range(self.board_size):
            merged_values = np.zeros(self.board_size, dtype=bool)
            for row in range(self.board_size - 1):
                if self.board_values[row, col] == self.board_values[row+1, col] and not merged_values[row] and not merged_values[row+1]:
                    self.board_values[row, col] *= 2
                    self.board_values[row+1, col] = 0
                    merged_values[row] = True
                    merged_values[row+1] = True
                
                

    def draw_board(self):
        self.screen.fill(self.blank_color)
        for row in range(self.board_size):
            for col in range(self.board_size):
                pygame.draw.rect(
                    self.screen,
                    self.cell_colors[self.board_values[row, col]],
                    self.cell_rects[row, col],
                )
                if self.board_values[row, col] != 0:
                    font = pygame.font.SysFont("Arial", 40, bold=True)
                    text = font.render(
                        str(self.board_values[row, col]), True, self.text_color
                    )
                    text_rect = text.get_rect(center=self.cell_rects[row, col].center)
                    self.screen.blit(text, text_rect)

        # pygame.display.update()
