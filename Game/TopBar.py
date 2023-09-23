import pygame


class TopBar:
    def __init__(self, screen: pygame.Surface, shift : int, x: int = 0, y: int = 0):
        self.screen = screen
        self.shift = shift
        self.top_bar = pygame.Surface(
            (self.screen.get_width(), shift)
        )
        self.top_bar.fill((255, 255, 255))
        self.screen.blit(self.top_bar, (0, 0))

        self.x = x
        self.y = y
        #self.score = 0
        self.best_score = 0

    def draw_top_bar(self, score : int = 0):
        self.screen.blit(self.top_bar, (self.x, self.y))
        self.draw_score(score=score)

    def draw_score(self, score : int = 0):
        font = pygame.font.SysFont("Arial", 30)
        text = font.render(f"Score: {score}", True, (0, 0, 0))
        # Center the text
        text_rect = text.get_rect(center=(self.screen.get_width() / 2, self.shift / 2))
        self.screen.blit(text, text_rect)

        """
        text = font.render(f"Best Score: {self.best_score}", True, (0, 0, 0))
        self.screen.blit(text, (self.x + 10, self.y + 50))
        """
