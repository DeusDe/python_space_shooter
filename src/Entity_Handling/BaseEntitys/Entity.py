import os
from os.path import join
import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self,display_surface,group,sprite_name = None,surface = None):
        super().__init__(group)


        if sprite_name:
            sprite_path = self.check_path(sprite_name)
            self.image = pygame.image.load(sprite_path).convert_alpha()
        elif surface:
            self.image = surface
        else:
            self.image = pygame.image.load('placeholder').convert_alpha()

        self.manager_id = 0
        self.manager = None
        self.rect = self.image.get_frect(center=(0, 0))

        self.display = display_surface

        self.speed = 1
        self.direction = pygame.math.Vector2(0, 0)


    def set_speed(self,speed):
        self.speed = speed

    def set_manager_id(self,manager_id):
        self.manager_id = manager_id

    def set_manager(self,manager):
        self.manager = manager

    def remove_from_manager(self):
        if self.manager:
            self.manager.remove_with_id(self.manager_id)
            self.kill()

    def reset_direction(self):
        self.direction = pygame.math.Vector2(0, 0)

    def normalize_direction(self):
        if self.direction:
            self.direction = self.direction.normalize()

    def get_speed(self):
        return self.speed

    def scale_picture(self,scale):
        self.image = pygame.transform.smoothscale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))

    def rotate_center(self,angle):
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_frect(center=self.rect.center)

    def colorize(self,color):
        self.image.fill(color, special_flags=pygame.BLEND_RGBA_MIN)

    def move_with_vector(self, delta):
        self.normalize_direction()
        self.rect.center += (self.direction * self.speed) * delta

    def set_center_position(self,x,y):
        self.rect.center = (x,y)

    def set_midbottom_position(self,pos):
        self.rect.midbottom = pos

    @staticmethod
    def check_path(sprite_name):
        if not sprite_name.endswith('.png'):
            sprite_name += '.png'
        sprite_path = join('images', sprite_name)
        if not os.path.isfile(sprite_path):
            print(f"Warning: Sprite '{sprite_name}' not found in 'images' directory.")
            return None
        return sprite_path