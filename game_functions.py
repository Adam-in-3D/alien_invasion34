import pygame
import sys
from bullets import Bullets
from aliens import Alien


def check_events(settings, screen, bullets, ship):
    # Checks for key/mouse events and responds accordingly
    # Loop to check for keypress events
    for event in pygame.event.get():
        # If escape key is press exit game
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            keydown_event(event, settings, screen, bullets, ship)
        elif event.type == pygame.KEYUP:
            keyup_event(event, ship)


# Defines the when the ship moves when a key is pressed
def keydown_event(event, settings, screen, bullets, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_z or event.key == pygame.K_SPACE:
        new_bullet = Bullets(settings, screen, ship)
        bullets.add(new_bullet)


# Defines that the ship should stay still when the key is not pressed
def keyup_event(event, ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        if event.key == pygame.K_LEFT:
            ship.moving_left = False
        if event.key == pygame.K_UP:
            ship.moving_up = False
        if event.key == pygame.K_DOWN:
            ship.moving_down = False

def create_fleet(settings, screen, aliens):
    alien = Alien(settings,screen)
    number_of_rows = alien.number_of_rows
    print(number_of_rows)
    number_of_aliens = alien.number_of_aliens
    print(number_of_aliens)

    for alien_number in range(number_of_aliens):
        for row_number in range(number_of_rows):
            alien_width = alien.rect.width
            alien_height = alien.rect.height
            alien.x = 2 * alien_width * alien_number
            print(alien.x)
            alien.rect.x = alien.x
            alien.y = 4 * alien_height * row_number
            print(alien.y)
            alien.rect.y = alien.y
            aliens.add(alien)



"""
def creating_fleet(settings, screen, ship, aliens):
    # Creating a fleet of aliens
    alien = Alien(settings, screen)
    number_of_aliens = get_number_of_aliens(settings, alien.rect.width)
    print(number_of_aliens)
    number_of_rows = get_number_rows(settings, alien.rect.height, ship.rect.height)
    print(number_of_aliens)

    for row_number in range(number_of_rows):
        for alien_number in range(number_of_aliens):
            create_alien(settings, screen, aliens, alien_number, row_number)


def get_number_of_aliens(settings, alien_width):
    # Determines the number of aliens in a row
    available_space_x = settings.screen_width - 2 * alien_width
    number_of_aliens = int(available_space_x/(2*alien_width))
    return number_of_aliens


def get_number_rows(settings, alien_height, ship_height):
    # Creates rows of aliens
    available_space_y = settings.screen_height - 3 * alien_height - 6 * ship_height
    number_of_rows = int(available_space_y/(2 * alien_height))
    return number_of_rows


def create_alien(settings, screen, aliens, alien_number, row_number):
    # Creates an alien and places it on a row
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = 2 * alien_width * alien_number
    alien.rect.x = alien.x

    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    # add the alien to the list of aliens
    aliens.add(alien)
"""

def update_screen(settings, screen, bullets, ship, aliens):
    # Fills screen with the background color
    screen.fill(settings.bg_color)

    # Draws ship on the screen
    ship.update()
    ship.blitme()

    # Draws aliens
    aliens.draw(screen)
    aliens.update()

    # Draws the bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Updating the display
    pygame.display.flip()

# def update_fleet():


def check_collision(bullets, aliens):
    pygame.sprite.groupcollide(bullets, aliens, True, True)
