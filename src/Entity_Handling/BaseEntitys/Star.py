from random import randint, uniform

from src.Entity_Handling.BaseEntitys.Entity import Entity
import pygame


class Star(Entity):
    def __init__(self, display_surface, group, surface):
        super().__init__(display_surface, group, surface=surface)

        # Initialize movement and random attributes
        self.direction = pygame.math.Vector2(0, 1)  # Downward direction
        self.speed =  uniform(5.0, 20.0)
        self.set_random_position()

        self.scale = uniform(0.25,0.65)
        self.angle = randint(0, 180)
        self.scale_and_rotate()

        # Apply random color with transparency
        color = (randint(20, 255), randint(0, 90), randint(20, 255), randint(150, 255))
        self.colorize(color)

    def set_random_position(self):
        """Sets the star to a random position within the display surface bounds."""
        x = randint(0, self.display.get_width())
        y = randint(0, self.display.get_height())
        self.set_center_position(x, y)

    def reset_position_to_top(self):
        """Resets the star's position to a random point just above the screen."""
        x = randint(0, self.display.get_width())
        self.set_center_position(x, -50)

    def update(self, delta):
        """Moves the star and resets its position if it exits the screen."""
        self.move_with_vector(delta)
        if self.rect.top > self.display.get_height():
            self.reset_position_to_top()

