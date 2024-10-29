from pygame.sprite import collide_mask

from src.Entity_Handling.Animation.Animation import Animation
from src.Entity_Handling.BaseEntitys.Entity import Entity
import pygame


class EntityManager:
    def __init__(self,display_surface,group,surface,type=Entity):
        self.display_surface=display_surface
        self.all_sprite_group=group
        self.sprite_group=pygame.sprite.Group()
        self.entity_type = type

        self.entity_surface = surface
        self.entities = {}
        self.id_counter = 1

    def remove_with_id(self,entity_id):
        entity = self.entities.pop(entity_id, None)
        if entity:
            entity.kill()

    def get_entity(self, entity_id: int):
        return self.entities.get(entity_id)

    def clear_all(self):
        """Removes all entities from the manager and the group."""
        for entity_id in list(self.entities.keys()):
            self.remove_with_id(entity_id)

    def collide_and_kill(self,collider):
        amount_killed = 0

        if type(collider) == pygame.sprite.Group:
            for entity in collider:
                collision = pygame.sprite.spritecollide(entity, self.sprite_group, False, pygame.sprite.collide_mask)
                if collision:
                    explosion = Animation(self.display_surface,self.all_sprite_group,'explosion',20)
                    explosion.set_center_position(entity.rect.centerx,entity.rect.centery)
                    amount_killed += 1
                    collision[0].remove_from_manager()
                    entity.remove_from_manager()



        else:
            collision = pygame.sprite.spritecollide(collider, self.sprite_group, False, pygame.sprite.collide_mask )
            if collision:
                amount_killed += 1
                collision[0].remove_from_manager()
        return amount_killed


    def add_entity(self):
        entity_id = self.id_counter
        entity = self.entity_type(self.display_surface,(self.all_sprite_group,self.sprite_group), surface=self.entity_surface)
        entity.set_manager_id(entity_id)
        entity.manager = self
        self.entities[entity_id] = entity
        self.id_counter = self.id_counter + 1
        return entity_id