import sys
import pygame
import random
from settings import Settings
from catcher import Catcher
from ball import Ball

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
        pygame.display.set_caption("Blue Window")

        self.catcher = Catcher(self)
        self.balls = pygame.sprite.Group()
        self.create_ball()
    
    def create_ball(self):
        ball = Ball(self)
        ball_width, ball_height = ball.rect.size
        ball.x = random.randint(ball_width, (self.settings.screen_width-ball_width))
        ball.rect.x = ball.x
        ball.rect.y = ball_height
        self.balls.add(ball)
    
    def check_ball_edges(self):
        for ball in self.balls.sprites():
            if ball.check_edges():
                ball.kill()
                self.create_ball()
                break
            else:
                return True

    def run_game(self):
        while True:
            self._check_events()
            self.catcher.update()
            self.update_ball()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        if self.settings.movement_keys == "1":
            if event.key == pygame.K_RIGHT:
                self.catcher.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.catcher.moving_left = True
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
        elif self.settings.movement_keys == "2":
            if event.key == pygame.K_d:
                self.catcher.moving_right = True
            elif event.key == pygame.K_a:
                self.catcher.moving_left = True
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
    
    def _check_keyup_events(self, event):
        if self.settings.movement_keys == "1":
            if event.key == pygame.K_RIGHT:
                self.catcher.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.catcher.moving_left = False
        elif self.settings.movement_keys == "2":
            if event.key == pygame.K_d:
                self.catcher.moving_right = False
            elif event.key == pygame.K_a:
                self.catcher.moving_left = False
    
    def update_ball(self):
        self.check_ball_edges()
        self.balls.update()
        if self.check_ball_edges() == True:
            for ball in self.balls.sprites():
                if pygame.sprite.spritecollideany(self.catcher, self.balls):
                    ball.kill()
                    self.create_ball()
                ball.rect.y += self.settings.fleet_drop_speed

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.catcher.blitme()
        self.balls.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    main = Window()
    main.run_game()