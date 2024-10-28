import pygame
from random import randint
from src.Entitys.Entity import Entity
from src.Entitys.Laser import Laser
from src.Entitys.Player import Player
from src.Entitys.Stars_Manager import Stars_Manager

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FRAMERATE = 60

# General Setup
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space shooter')
clock = pygame.time.Clock()
running = True
# surface
surface = pygame.Surface((100, 200))
x = 100
y = 150

all_sprites = pygame.sprite.Group()

# importing image


star_manager = Stars_Manager(pygame,display_surface,all_sprites,20)
player = Player(pygame,display_surface,all_sprites)

# Game Loop
while running:

    def events():
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                global running
                running = False

    delta = clock.tick() / 1000 # Limit to 60 Frames
    print(int(clock.get_fps()), delta)
    events()

    star_manager.update(delta)


    all_sprites.update(delta=delta)
    display_surface.fill('black')
    all_sprites.draw(display_surface)
    pygame.display.update()
    #generate_frame()




pygame.quit()