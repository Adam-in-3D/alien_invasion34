import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen
        # Loading ship image, and it's rectangle
        # Loads the ship from its image data
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        # interpret the self.image as a rectangle
        self.rect = self.image.get_rect()
        # Computer will now interpret the screen as a rectangle
        self.screen_rect = screen.get_rect()

        # Start ship at the bottom center of the screen
        # Makes the center x value of the ship the same as the center x value of the screen
        self.rect.centerx = self.screen_rect.centerx
        # Makes the bottom of the ship the same as the bottom of the screen
        self.rect.bottom = self.screen_rect.bottom

        # Stores center x  & y of the ship as a decimal value
        self.center = float(self.rect.centerx)
        self.center2 = float(self.rect.centery)

        # Create movement flags to determine if the ship is moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        # Draws the ship on the screen
        # image.blit(image being added, location)
        self.screen.blit(self.image, self.rect)

    def update(self):
        # Updates the image of the ship and keeps it on screen
        if self.moving_right and self.center < 885:
            # Above can also do "and self.rect.right < self.screen.right
            self.center += .5
        elif self.moving_left and self.center > 15:
            # Above can also do "and self.rect.left < self.screen.left
            self.center -= .5
        if self.moving_up and self.center2 > 20:
            self.center2 -= .5
        elif self.moving_down and self.center2 < 660:
            self.center2 += .5
        # Updates rect from self.center
        self.rect.centerx = self.center
        self.rect.centery = self.center2