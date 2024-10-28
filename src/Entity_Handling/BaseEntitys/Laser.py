from src.Entity_Handling.BaseEntitys.Entity import Entity


class Laser(Entity):
    def __init__(self,display_surface,group,surface):
        Entity.__init__(self,display_surface,group,surface=surface)
        self.speed = 400


    def update(self,delta):
        self.rect.y -= self.speed * delta

        if self.rect.y < -50:
            self.remove_from_manager()