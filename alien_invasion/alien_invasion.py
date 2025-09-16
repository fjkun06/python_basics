import sys
import pygame

# custom modules
from settings import Settings
from ship import Ship
from music_player import play_music

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.clock = pygame.time.Clock()  #
        self.ship = Ship(self)
        pygame.display.set_caption("Alien Invasion")
        
        #Play Background sound
        play_music()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events
            self._check_events()
            # Redraw the screen during each pass through the loop.
            self._update_screens()
            # Make the most recently drawn screen visible
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screens(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
