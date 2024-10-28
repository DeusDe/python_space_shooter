from src.Entity_Handling.EntityManager.EntityManager import EntityManager
from src.Entity_Handling.BaseEntitys.Star import Star
import pygame

class StarManager(EntityManager):
    def __init__(self,display_surface,group,start_amount):
        surface = pygame.image.load(Star.check_path('star')).convert_alpha()
        super().__init__(pygame,display_surface,group,surface,type=Star)

        for i in range(start_amount):
            self.addEntity()

