# Import Pygame Module
import pygame

class SpaceShip:

    # Constructor
    def __init__(self, image, x, y):
        self.image = image  # Image of the spaceship
        self.x = x  # X-coordinate of the spaceship
        self.y = y  # Y-coordinate of the spaceship
        self.rect = pygame.Rect((x, y), self.image.get_size())  # Rectangular area of the spaceship image

    # Move SpaceShip Down
    def move_down(self, win, velocity):
        # Check if moving down will keep the spaceship within the window's boundaries
        if self.rect.midbottom[1] < (win.get_height() - 14):
            return self.y + velocity  # Move down by the given velocity
        else:
            return self.y  # Stay at the current position

    # Move SpaceShip Left
    def move_left(self, win, velocity):
        # Check if moving left will keep the spaceship within the window's boundaries
        if self.rect.midleft[0] > ((win.get_width() - win.get_width()) + 10):
            return self.x - velocity  # Move left by the given velocity
        else:
            return self.x  # Stay at the current position

    # Move SpaceShip Right
    def move_right(self, win, velocity):
        # Check if moving right will keep the spaceship within the window's boundaries
        if self.rect.midright[0] < (win.get_width() - 14):
            return self.x + velocity  # Move right by the given velocity
        else:
            return self.x  # Stay at the current position

    # Get the Position of the SpaceShip
    def get_position(self):
        return (self.x, self.y)  # Return the current position as a tuple

    # Get the Resolution of the SpaceShip's Image
    def get_resolution(self):
        return self.image.get_size()  # Return the image resolution as a tuple
