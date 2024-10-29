from random import randint, uniform

from src.Entity_Handling.BaseEntitys.Entity import Entity
import pygame

class Meteor(Entity):
    def __init__(self,display_surface,group,surface):
        super().__init__(display_surface,group,surface=surface)

        self.set_initial_position_and_direction()
        self.set_speed(randint(100, 300))
        self.scale = randint(50, 100) / 100
        self.angle = randint(0, 180)
        self.rotation_speed =randint(20,40)
        self.scale_and_rotate()

    def set_initial_position_and_direction(self):
        """Sets the initial position above the screen and a random horizontal direction."""
        self.set_center_position(randint(0, self.display.get_width()), -100)
        self.direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1)

    def update(self, delta):
        """Moves the meteor and removes it if it exits the screen."""
        self.move_with_vector(delta)
        if self.rect.top > self.display.get_height():
            self.remove_from_manager()

        self.set_angle(self.angle+(self.rotation_speed*delta))
