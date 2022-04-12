# Class to store all settings
class Settings():
    # Initialize game settings
    def __init__(self):
        # Screen settings
        self.screen_width = 900
        self.screen_height = 680
        self.bg_color = (25, 0, 50)

        # Bullet settings
        self.bullet_speed = .5
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_color = (0, 255, 0)

        # Player settings
        self.lives = 3
        self.score = 0
