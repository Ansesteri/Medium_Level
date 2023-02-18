import sys
import pygame
from settings import Settings
from stars import Star

class Window:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        if self.settings.fullscreen == True:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        elif self.settings.fullscreen == False:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Stars")

        self.stars = pygame.sprite.Group()
        self._create_stars()
    
    def _create_stars(self):
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - (2*star_width)
        number_stars_x = ((available_space_x // (2*star_width)) + 1)
        available_space_y = self.settings.screen_height - (3 * star_height)
        number_rows = available_space_y // (2*star_height)

        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self.create_star(star_number, row_number)
        
    def create_star(self, star_number, row_number):
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star_height + 2 * star_height * row_number
        self.stars.add(star)
    
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                
    def _check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    main = Window()
    main.run_game()