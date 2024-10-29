from src.Entity_Handling.EntityManager.EntityManager import EntityManager
from src.Entity_Handling.BaseEntitys.Star import Star
import pygame

class StarManager(EntityManager):
    def __init__(self,display_surface,group,start_amount):
        surface = pygame.image.load(Star.check_path('star')).convert_alpha()
        super().__init__(display_surface,group,surface,type=Star)
        self.add_initial_stars(start_amount)  # Add initial stars

    def add_initial_stars(self, amount):
        """Adds the initial amount of stars to the manager."""
        for _ in range(amount):
            self.add_entity()