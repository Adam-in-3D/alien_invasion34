import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    # Class to manage bullet fire from ship
    def __init__(self, settings, screen, ship):
        # Initalize bullet object and tracks position on the screen
        super(Bullets, self). __init__()
        self.screen = screen

        # Creating bullet rectangle
        # Creating rectangular bullet at 0,0
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        # Moves bullet to the center top of the ship
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Saving bullet position as a decimal value
        self.y = float(self.rect.y)

        # Gives color to the bullets
        self.color = settings.bullet_color

        # Assign speed to bullets
        self.speed = settings.bullet_speed

    def update(self):
        # Move the bullet on screen
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        # Creates bullet on screen
        pygame.draw.rect(self.screen, self.color, self.rect)
