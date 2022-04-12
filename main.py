# Imports pygame and system features
import pygame
# imports other libraries to be used
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


# Function that allows the game to run
def alien_invasion():
    # Initializes pygame
    pygame.init()
    settings = Settings()
    # Creates screen with dimensions of the width and height (Screen is a hidden class, and it's calling a method)
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    # Names the window
    pygame.display.set_caption('Space Dudes That Shoot Missississles')

    # Adds the ship
    ship = Ship(screen)

    # Making a group to store the bullets and aliens
    bullets = Group()
    aliens = Group()

    # gf.creating_fleet(settings, screen, ship, aliens)
    gf.create_fleet(settings, screen, aliens)

    # Loop to start animation
    while True:
        gf.check_events(settings, screen, bullets, ship)
        bullets.update()
        gf.update_screen(settings, screen, bullets, ship, aliens)
        gf.check_collision(bullets, aliens)
        # aliens.update()

        print(len(aliens))







alien_invasion()
