import pygame
from pygame.sprite import Sprite


# Class that represents one alien from the fleet
class Alien(Sprite):
    def __init__(self, settings, screen, ):
        super(Alien, self).__init__()

        # Defines the attributes
        self.screen = screen
        self.settings = settings

        # Loads the image from the images folder
        self.image = pygame.image.load("images/alien.png")
        # Scales the alien ship
        self.image = pygame.transform.scale(self.image, (40, 20))
        # Gets the rectangular properties
        self.rect = self.image.get_rect()

        # Defines the starting location
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Allows x position to handle decimals
        self.x = float(self.rect.x)

        # Spacing of the aliens
        self.available_space_x = self.settings.screen_width - (2 * self.rect.width)
        self.number_of_aliens = int(self.available_space_x / (2 * self.rect.width))

        self.available_space_y = self.settings.screen_height - (2 * self.rect.height)
        self.number_of_rows = int(self.available_space_y / (2 * self.rect.height))

        self.rect.x = self.x
        self.speed = 1
        self.direction = 1

    def blitme(self):
        # Draws the alien on the screen
        # image.blit(image being added, location)
        self.screen.blit(self.image, self.rect)

    def update(self):
        # Moves alien
        self.x = self.speed * self.direction
        self.rect.x = self.x

    def check_screen(self):
        # Checks if the aliens hit the edge of the screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
