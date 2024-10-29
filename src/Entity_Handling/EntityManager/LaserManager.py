from src.Entity_Handling.BaseEntitys.Laser import Laser
from src.Entity_Handling.EntityManager.EntityManager import EntityManager
import pygame

class LaserManager(EntityManager):
    def __init__(self,display_surface,group):
        surface = pygame.image.load(Laser.check_path('laser')).convert_alpha()
        super().__init__(display_surface,group,surface,type=Laser)

    def add_laser_at_position(self, pos):
        id = self.add_entity()
        self.entities[id].set_midbottom_position(pos)
