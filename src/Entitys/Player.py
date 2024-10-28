

from src.Entitys.Entity import Entity


class Player(Entity):
    def __init__(self,pygame,display_surface,groups):
        Entity.__init__(self,pygame,display_surface,groups,'player')
        self.speed = 250
        self.set_center_position(display_surface.get_width()/2,display_surface.get_height()/2)

    def update(self,delta):
        keys = self.get_pressed_keys()

        self.reset_direction()

        self.direction.y = int(keys[self.pygame.K_DOWN] or keys[self.pygame.K_s]) - int(keys[self.pygame.K_UP] or keys[self.pygame.K_w])
        self.direction.x = int(keys[self.pygame.K_RIGHT] or keys[self.pygame.K_d]) - int(keys[self.pygame.K_LEFT] or keys[self.pygame.K_a])

        recent_keys = self.get_just_pressed_keys()
        if recent_keys[self.pygame.K_SPACE] :
            print('Fire Laser')

        self.move_with_vector(delta)



