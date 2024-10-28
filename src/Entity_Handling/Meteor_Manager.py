from random import randint

from src.Entity_Handling.BaseEntitys.Entity import Entity


class Meteor_Manager():
    def __init__(self,pygame,display_surface,group,meteor_amount):
        self.pygame=pygame
        self.display_surface=display_surface
        self.group=group


        self.meteor_surface = pygame.image.load(Entity.check_path('meteor')).convert_alpha()
        self.meteors = []
        pass

    def new_meteor(self):
        meteor = Entity(self.pygame,self.display_surface,self.group,surface=self.meteor_surface)
        meteor.set_speed(randint(100, 300) / 10)
        meteor.direction.y = 1
        meteor.set_center_position(randint(0, self.display_surface.get_width()), 0)
        self.meteors.append(meteor)

    def update(self, delta):

        for meteor in self.meteors:
            meteor.move_with_vector(delta)
            meteor.update(delta)
            if meteor.rect.y > meteor.display.get_height():
                meteor.remove_from_manager()