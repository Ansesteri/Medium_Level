import sys
import pygame
from settings import Settings
from stars2 import Star
from time import sleep

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
        pygame.display.set_caption("Rain")

        self.stars = pygame.sprite.Group()
        self._create_stars()
    
    def _create_stars(self):
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - (2*star_width)
        number_stars_x = ((available_space_x // (2*star_width)) + 0)
        available_space_y = self.settings.screen_height - (3 * star_height)
        number_rows = (available_space_y // (2*star_height)) + 1

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
    
    def _check_star_bottom(self):
        for star in self.stars.sprites():
            if self.settings.moving_down == True:
                self._star_drop()
                break
    
    def _star_drop(self):
        screen_rect = self.screen.get_rect()
        for star in self.stars.sprites():
            if not star.rect.bottom >= screen_rect.bottom:
                star.rect.y += self.settings.fleet_drop_speed
            else:
                star.kill()
    
    def run_game(self):
        while True:
            self._check_events()
            self.update_stars()
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
    
    def update_stars(self):
        self._check_star_bottom()
        self._star_drop()
        self.stars.update()
        sleep(0.2)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    main = Window()
    main.run_game()