from src.Entity_Handling.BaseEntitys.Entity import Entity
import pygame


class Laser(Entity):
    def __init__(self,display_surface,group,surface):
        super().__init__(display_surface,group,surface=surface)
        self.speed = 400
        self.direction = pygame.math.Vector2(0, -1)  # Set direction to move upwards

    def update(self, delta):
        """Moves the laser upwards and removes it if it goes off-screen."""
        self.move_with_vector(delta)  # Move laser with predefined method
        if self.rect.bottom < 0:
            self.remove_from_manager()  # Remove when off-screen