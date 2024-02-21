# Import the Pygame module
import pygame

class CannonBall:

    # Constructor
    def __init__(self, image, x, y):
        self.image = image  # Image of the cannonball
        self.x = x  # X-coordinate of the cannonball
        self.y = y  # Y-coordinate of the cannonball
        self.rect = pygame.Rect((x, y), self.image.get_size())  # Rectangular area of the cannonball image

    # Move the CannonBall Up
    def move_up(self, velocity):
        return self.y - velocity  # Move the cannonball up by the given velocity

    # Get the Position of the CannonBall
    def get_position(self):
        return (self.x, self.y)  # Return the current position as a tuple

    # Get the Resolution of the CannonBall's Image
    def get_resolution(self):
        return self.image.get_size()  # Return the image resolution as a tuple
