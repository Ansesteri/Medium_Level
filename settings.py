class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200, 200, 200)
        self.fullscreen = True

        # 1 = Arrow control, 2 = WASD control
        self.movement_keys = "2"
        self.ship_limit = 3

        self.bullet_width = 1920
        self.bullet_height = 600
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        self.fleet_drop_speed = 10
        self.moving_down = True
        
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialyze_dynamic_settings()
    
    def initialyze_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1.5
        self.alien_speed_factor = 1.0
        self.difficulty = 0.5

        self.fleet_direction = 1

        self.alien_points = 50
    
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.difficulty *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)