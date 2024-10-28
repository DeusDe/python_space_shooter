from src.Entity_Handling.BaseEntitys.Entity import Entity
import pygame


class EntityManager:
    def __init__(self,pygame,display_surface,group,surface,type=Entity):
        pygame=pygame
        self.display_surface=display_surface
        self.group=group

        self.entity_type = type

        self.entity_surface = surface
        self.entitys = {}
        self.id_counter = 1

    def remove_with_id(self,id):
        if id in self.entitys:
            self.entitys.pop(id)

    def addEntity(self):
        id = self.id_counter
        entity = self.entity_type(self.display_surface,self.group,surface=self.entity_surface)
        entity.set_manager_id(id)
        entity.manager = self
        self.entitys[id] = entity
        self.id_counter = self.id_counter + 1
        return id