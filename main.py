import pygame

from src.Entity_Handling.Animation.Animation import Animation
from src.Entity_Handling.BaseEntitys.Player import Player
from src.Entity_Handling.EntityManager.StarManager import StarManager
from src.Entity_Handling.EntityManager.MeteorManager import MeteorManager
from src.UI.UIManager import UIManager

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FRAMERATE = 60

# General Setup
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
clock = pygame.time.Clock()
running = True

# Sprites Group
all_sprites = pygame.sprite.Group()

# Importing Fonts
ui_manager = UIManager()

# Importing Entitys
star_manager = StarManager( display_surface, all_sprites, 100)
meteor_manager = MeteorManager( display_surface, all_sprites)
player = Player(display_surface, all_sprites)

# Custom event -> meteor spawn event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)

score_event = pygame.event.custom_type()
pygame.time.set_timer(score_event, 1000)

player.set_meteor_manager(meteor_manager)

# Event Handling
def handle_events():
    global running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            meteor_manager.add_entity()
        if event.type == score_event:
            if player.is_alive:
                player.score += 2

def update_screen():
    display_surface.fill('black')
    all_sprites.draw(display_surface)
    ui_manager.draw_ui(display_surface)
    pygame.display.update()


def run_game():
    global running

    while running:
        delta = clock.tick() / 1000  # Limit to 60 Frames
        handle_events()

        if player.is_alive:
            all_sprites.update(delta=delta)

        ui_manager.update_ui(player.score, player.hp)
        update_screen()

run_game()

pygame.quit()