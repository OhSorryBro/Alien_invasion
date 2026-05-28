import sys
import pygame

class AlienInvasion:
    """Class for managing resourses and working of the game"""

    def __init__(self):
        """Initialisation of the game nad it's resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien invasion")
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Starting the game loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                self.screen.fill((self.bg_color))
                pygame.display.flip()
                self.clock.tick(60)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()