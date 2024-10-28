from random import randint

from src.Entity_Handling.BaseEntitys.Entity import Entity
import pygame

class Star(Entity):
    def __init__(self,display_surface,group,surface):
        Entity.__init__(self,display_surface,group,surface=surface)

        self.direction.y = 1
        self.set_center_position(randint(0, display_surface.get_width()), randint(0, display_surface.get_height()))
        self.set_speed(randint(100, 300) / 10)
        self.scale_picture(randint(25, 60) / 100)
        self.rotate_center(randint(0, 180))
        self.colorize((randint(20, 255), randint(0, 90), randint(20, 255), randint(150, 255)))

    def set_ran_pos(self):
        self.set_center_position(randint(0, self.display.get_width()), -50)

    def update(self,delta):
        self.move_with_vector(delta)
        if self.rect.y > self.display.get_height():
            self.set_ran_pos()

