import os
from os.path import join
import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self,display_surface,group,sprite_name = None,surface = None):
        super().__init__(group)


        if sprite_name:
            sprite_path = self.check_path(sprite_name)
            if sprite_path:
                self.original_image = pygame.image.load(sprite_path).convert_alpha()
            else:
                self.original_image = pygame.Surface((50, 50))  # Fallback placeholder
                self.original_image.fill((255, 0, 0))  # Red to indicate missing image
        elif surface:
            self.original_image = surface
        else:
            self.original_image = pygame.Surface((50, 50))  # Default placeholder
            self.original_image.fill((255, 0, 0))


        self.image = self.original_image

        self.manager_id = 0
        self.manager = None
        self.rect = self.image.get_frect(center=(0, 0))

        self.display = display_surface

        self.speed = 1
        self.direction = pygame.math.Vector2(0, 0)

        self.mask = pygame.mask.from_surface(self.image)
        self.mask_surface = self.mask.to_surface()
        self.scale = 1
        self.angle = 0

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
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()

    def get_speed(self):
        return self.speed

    def scale_picture(self, scale):
        if scale > 0:  # Ensure scale is a positive value
            new_width = int(self.image.get_width() * scale)
            new_height = int(self.image.get_height() * scale)
            self.image = pygame.transform.smoothscale(self.image, (new_width, new_height))
            self.rect = self.image.get_frect(center=self.rect.center)
        else:
            print("Warning: Scale must be a positive value.")

    def rotate_image(self, angle):
        self.image = pygame.transform.rotozoom(self.image, angle,1)
        self.rect = self.image.get_frect(center=self.rect.center)

    def set_angle(self,angle):
        self.angle = angle
        self.scale_and_rotate()

    def set_scale(self,scale):
        self.scale = scale
        self.scale_and_rotate()

    def scale_and_rotate(self):
        self.image = self.original_image
        self.scale_picture(self.scale)
        self.rotate_image(self.angle)
        self.generate_new_mask()


    def generate_new_mask(self):
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_surface = self.mask.to_surface()



    def colorize(self,color):
        self.image.fill(color, special_flags=pygame.BLEND_RGBA_MIN)

    def move_with_vector(self, delta):
        self.normalize_direction()
        movement = self.direction * self.speed * delta
        self.rect.center += movement

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