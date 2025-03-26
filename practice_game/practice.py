import pygame
import sys

class Practice:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()

    def _check_events(self):
        for event in pygame.event.get():
                # quitting the game when the event from the user is processed to exit
                if event == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
            pygame.display.flip()
            self.screen.fill((0, 164, 194))

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

if __name__ == "__main__":
    practice_game = Practice()
    practice_game.run_game()