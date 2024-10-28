from src.Entity_Handling.BaseEntitys.Laser import Laser
from src.Entity_Handling.EntityManager.EntityManager import EntityManager


class LaserManager(EntityManager):
    def __init__(self,pygame,display_surface,group):
        surface = pygame.image.load(Laser.check_path('laser')).convert_alpha()
        super().__init__(pygame,display_surface,group,surface,type=Laser)

    def addEntityPos(self,pos):
        id = self.addEntity()
        self.entitys[id].set_midbottom_position(pos)