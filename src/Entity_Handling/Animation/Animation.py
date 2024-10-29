
from os.path import join
import pygame

from src.Entity_Handling.BaseEntitys.Entity import Entity


class Animation(Entity):
    def __init__(self,display_surface,group,folder_name,animation_length):
        super().__init__( display_surface,group,'star')

        self.frames = []
        self.frame_index = 0
        self.animation_length = animation_length

        for i in range(animation_length):
            path = self.check_path(join(folder_name, f'{i}.png'))
            print(path)
            if not path is None:
                self.frames.append(pygame.image.load(path).convert_alpha())

        if len(self.frames) == animation_length:
            self.image = self.frames[self.frame_index]
            self.original_image = self.image
            self.rect = self.image.get_frect()
        else:
            print('Images could not be loaded')
            self.kill()


    def set_frame(self,frame):
        self.original_image = self.frames[frame]
        self.scale_and_rotate()

    def update(self,delta):
        if self.frame_index > self.animation_length-1:
            self.kill()
        self.set_frame(int(self.frame_index))
        self.frame_index += 30 * delta
