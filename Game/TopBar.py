import pygame

class TopBar:
    def __init__(self, screen : pygame.Surface):
        self.screen = screen
        self.top_bar = pygame.Surface((self.screen.get_width(), self.screen.get_height() // 10))
        self.top_bar.fill((255, 255, 255))
        self.screen.blit(self.top_bar, (0, 0))

    def draw_top_bar(self):
        self.screen.blit(self.top_bar, (0, 0))