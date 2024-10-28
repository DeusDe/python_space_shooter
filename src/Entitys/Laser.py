from src.Entitys.Entity import Entity


class Laser(Entity):
    def __init__(self,pygame,display_surface,groups):
        Entity.__init__(self,pygame,display_surface,groups,'laser')