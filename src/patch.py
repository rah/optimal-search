from random import random
from math import cos, sin, radians
from entity import Entity


def rnd_direction():
    return radians(random() * 360.00)


class Patch(Entity):
    '''
    A patch contains a set of entities and is a type of entity in that
    it has a position and it's energy is the sum of all entities it contains.
    '''

    def __init__(
            self,
            x_pos=0.0,
            y_pos=0.0,
            radius=0.0):

        Entity.__init__(self, x_pos, y_pos)

        self.radius = radius
        self.entities = []

    def __str__(self):
        return "<Patch x:%s y:%s r:%s n:%s>" % (
            self.x_pos, self.y_pos, self.radius, len(self.entities))

    def add_entity(self, entity=None):
        '''
        Add an entity to a random position in patch
        '''
        if entity is None:
            entity = Entity()

        entity.x_pos, entity.y_pos = self.rnd_patch_position()

        self.entities.append(entity)

    def create_entities(self, n_entity):
        '''
        Create a set of entities
        '''
        for i in range(n_entity):
            self.add_entity()

    def rnd_patch_position(self):
        '''
        Get a random position in the patch
        '''
        x = self.x_pos + (self.rnd_radius() * cos(rnd_direction()))
        y = self.y_pos + (self.rnd_radius() * sin(rnd_direction()))

        return x, y

    def rnd_radius(self):
        '''
        Get a random length of the radius of the patch
        '''
        return random() * self.radius

