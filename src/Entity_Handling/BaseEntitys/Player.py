from src.Entity_Handling.BaseEntitys.Entity import Entity
from src.Entity_Handling.EntityManager.LaserManager import LaserManager
import pygame


class Player(Entity):
    def __init__(self,display_surface,group,speed=250,cooldown_duration=400):
        super().__init__(display_surface, group, 'player')

        # Initial position in the center of the display
        self.speed = speed
        self.set_center_position(display_surface.get_width() / 2, display_surface.get_height() / 2)

        # Shooting attributes
        self.score = 0
        self.hp = 5
        self.meteor_manager = None
        self.can_shoot = True
        self.is_alive = True
        self.laser_shooter_timer = 0
        self.cooldown_duration = cooldown_duration
        self.laser_manager = LaserManager(display_surface, group)

        self.scale = 1

    def laser_timer(self):
        """Handles the laser cooldown timer."""
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shooter_timer > self.cooldown_duration:
                self.can_shoot = True

    def handle_movement(self):
        """Handles the player's movement based on keyboard input."""
        keys = pygame.key.get_pressed()
        self.reset_direction()

        # Determine direction based on keys pressed
        self.direction.y = int(keys[pygame.K_DOWN] or keys[pygame.K_s]) - int(keys[pygame.K_UP] or keys[pygame.K_w])
        self.direction.x = int(keys[pygame.K_RIGHT] or keys[pygame.K_d]) - int(keys[pygame.K_LEFT] or keys[pygame.K_a])

    def set_meteor_manager(self,meteor_manager):
        self.meteor_manager = meteor_manager

    def reduce_hp(self,reduction):
        self.hp -= reduction
        if self.hp <= 0:
            self.is_alive = False

    def player_hit(self):
        if self.meteor_manager:
            if self.meteor_manager.collide_and_kill(self):
                self.reduce_hp(1)


    def laser_hit(self):
        if self.meteor_manager:
            meteor_killed = self.meteor_manager.collide_and_kill(self.laser_manager.sprite_group)
            self.score += meteor_killed * 5


    def handle_shooting(self):
        """Handles shooting logic and cooldown."""
        self.laser_timer()
        recent_keys = pygame.key.get_just_pressed()

        # Check for shooting with space key
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            print('Fire Laser')
            self.can_shoot = False
            self.laser_shooter_timer = pygame.time.get_ticks()
            self.laser_manager.add_laser_at_position(self.rect.midtop)

    def update(self, delta):
        """Updates the player by handling movement and shooting, and applying movement."""
        if not self.is_alive:
            return
        self.handle_movement()
        self.handle_shooting()
        self.move_with_vector(delta)

        self.laser_hit()
        self.player_hit()


