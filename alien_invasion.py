import sys
import pygame

class AlienInvasion:
    """Class for managing resourses and working of the game"""

    def __init__(self):
        """Initialisation of the game nad it's resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien invasion")

    def run_game(self):
        """Starting the game loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()