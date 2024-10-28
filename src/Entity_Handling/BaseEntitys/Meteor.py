from random import randint, uniform

from src.Entity_Handling.BaseEntitys.Entity import Entity


class Meteor(Entity):
    def __init__(self,display_surface,group,surface):
        Entity.__init__(self,display_surface,group,surface=surface)

        self.direction.y = 1
        self.direction.x = uniform(-0.5,0.5)
        self.set_speed(randint(100, 300) )
        self.scale_picture(randint(50, 100) / 100)
        self.rotate_center(randint(0, 180))
        self.set_center_position(randint(0, display_surface.get_width()), -100)
        self.is_destroyed = False


    def update(self,delta):
        self.move_with_vector(delta)
        if self.rect.y > self.display.get_height():
            self.remove_from_manager()


