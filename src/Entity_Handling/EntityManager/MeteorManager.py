from src.Entity_Handling.BaseEntitys.Meteor import Meteor
from src.Entity_Handling.EntityManager.EntityManager import EntityManager
import pygame

class MeteorManager(EntityManager):
    def __init__(self,display_surface,group):
        surface = pygame.image.load(Meteor.check_path('meteor')).convert_alpha()
        super().__init__(pygame,display_surface,group,surface,type=Meteor)









