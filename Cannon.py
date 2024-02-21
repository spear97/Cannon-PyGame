# Import the Pygame module
import pygame

class Cannon:

    # Constructor
    def __init__(self, image, x, y):
        self.image = image  # Image of the cannon
        self.x = x  # X-coordinate of the cannon
        self.y = y  # Y-coordinate of the cannon
        self.rect = pygame.Rect((x, y), self.image.get_size())  # Rectangular area of the cannon image

    # Move Cannon to the Right
    def move_right(self, win, velocity):
        # Check if moving right will keep the cannon within the window's boundaries
        if self.rect.midright[0] < (win.get_width() - 14):
            return self.x + velocity  # Move right by the given velocity
        else:
            return self.x  # Stay at the current position

    # Move Cannon to the Left
    def move_left(self, win, velocity):
        # Check if moving left will keep the cannon within the window's boundaries
        if self.rect.midleft[0] > ((win.get_width() - win.get_width()) + 10):
            return self.x - velocity  # Move left by the given velocity
        else:
            return self.x  # Stay at the current position

    # Get the Position of the Cannon
    def get_position(self):
        return (self.x, self.y)  # Return the current position as a tuple

    # Get the Resolution of the Cannon's Image
    def get_resolution(self):
        return self.image.get_size()  # Return the image resolution as a tuple
