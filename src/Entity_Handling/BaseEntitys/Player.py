

from src.Entity_Handling.BaseEntitys.Entity import Entity
from src.Entity_Handling.EntityManager.LaserManager import LaserManager
import pygame

class Player(Entity):
    def __init__(self,display_surface,group):
        Entity.__init__(self,display_surface,group,'player')
        self.speed = 250
        self.set_center_position(display_surface.get_width()/2,display_surface.get_height()/2)
        self.can_shoot = True
        self.laser_shooter_timer = 0
        self.cooldown_duration = 400
        self.laser_manager = LaserManager(pygame,display_surface,group)

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shooter_timer > self.cooldown_duration:
                self.can_shoot = True


    def update(self,delta):
        self.laser_timer()
        keys = pygame.key.get_pressed()

        self.reset_direction()

        self.direction.y = int(keys[pygame.K_DOWN] or keys[pygame.K_s]) - int(keys[pygame.K_UP] or keys[pygame.K_w])
        self.direction.x = int(keys[pygame.K_RIGHT] or keys[pygame.K_d]) - int(keys[pygame.K_LEFT] or keys[pygame.K_a])

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            print('Fire Laser')
            self.can_shoot = False
            self.laser_shooter_timer = pygame.time.get_ticks()
            self.laser_manager.addEntityPos(self.rect.midtop)

        self.move_with_vector(delta)



