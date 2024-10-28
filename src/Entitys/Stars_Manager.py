from random import randint, random

from src.Entitys.Entity import Entity


class Stars_Manager():
    def __init__(self,pygame,display_surface,group,star_amount,):
        self.stars = [Entity(pygame,display_surface,group,'star') for i in range(star_amount)]

        for star in self.stars:
            star.direction.y = 1
            star.set_center_position(randint(0,display_surface.get_width()),randint(0,display_surface.get_height()))
            star.set_speed(randint(100,300)/10)
            star.scale_picture(randint(25,60)/100)
            star.rotate_center(randint(0,180))
            star.colorize((randint(20,255),randint(0,90), randint(20,255), randint(150,255)))


    def update(self,delta):
        for star in self.stars:
            star.move_with_vector(delta)
            if star.rect.y > star.display.get_height():
                star.set_center_position(randint(0, star.display.get_width()), -50)


