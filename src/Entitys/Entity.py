import os
from os.path import join
import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self,pygame,display_surface,group,sprite_name):
        super().__init__(group)

        sprite_path = self.check_path(sprite_name)

        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.rect = self.image.get_frect(center=(0, 0))

        self.display = display_surface
        self.pygame = pygame

        self.speed = 1
        self.direction = self.pygame.math.Vector2(0, 0)


    def set_speed(self,speed):
        self.speed = speed

    def get_mouse_pos(self):
        return self.pygame.mouse.get_pos()

    def get_rel_mouse_pos(self):
        return self.pygame.mouse.get_rel()

    def get_mouse_pressed(self):
        return self.pygame.mouse.get_pressed()

    def get_leftclick(self):
        return self.pygame.mouse.get_pressed()[0]

    def get_middleclick(self):
        return self.pygame.mouse.get_pressed()[1]

    def get_rightclick(self):
        return self.pygame.mouse.get_pressed()[2]

    def get_pressed_keys(self):
        return self.pygame.key.get_pressed()

    def get_just_pressed_keys(self):
        return self.pygame.key.get_just_pressed()

    def reset_direction(self):
        self.direction = self.pygame.math.Vector2(0, 0)

    def normalize_direction(self):
        if self.direction:
            self.direction = self.direction.normalize()

    def get_speed(self):
        return self.speed

    def scale_picture(self,scale):
        self.image = self.pygame.transform.smoothscale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))

    def rotate_center(self,angle):
        self.image = self.pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_frect(center=self.rect.center)

    def colorize(self,color):
        self.image.fill(color, special_flags=self.pygame.BLEND_RGBA_MIN)

    def move_with_vector(self, delta):
        self.normalize_direction()
        self.rect.center += (self.direction * self.speed) * delta

    def set_center_position(self,x,y):
        self.rect.center = (x,y)

    def set_bottomleft_position(self,x,y):
        self.rect.bottomleft = (x,y)

    def set_bottomright_position(self,x,y):
        self.rect.bottomright = (x,y)

    def increase_x_position(self,inc_value):
        self.rect.left += inc_value

    def increase_y_position(self,inc_value):
        self.rect.bottom += inc_value

    def out_of_bounds(self):
        out = []
        if self.rect.right > self.display.get_width():
            out.append('RIGHT')
        if self.rect.left < 0:
            out.append('LEFT')
        if self.rect.top < 0:
            out.append('TOP')
        if self.rect.bottom > self.display.get_height():
            out.append('BOTTOM')
        if not out:
            return False
        return out

    def draw_entity(self):
        self.display.blit(self.image, self.rect)

    @staticmethod
    def check_path(sprite_name):
        if '.png' not in sprite_name:
            sprite_name = sprite_name + '.png'

        if sprite_name not in os.listdir('images'):
            return False

        return join('images', sprite_name)