from random import random
from math import cos, sin, radians

from src.simulation.entity import Entity


def rnd_direction():
    return radians(random() * 360.00)


class Patch(Entity):
    '''
    A patch contains a set of entities and is a type of entity in that
    it has a position and it's energy is the sum of all entities it contains.

    A patch is circular and therefore has a radius.
    '''

    def __init__(
            self,
            x_pos=0.0,
            y_pos=0.0,
            parent=None,  # A patch generally has an environment for a parent
            children=None,
            radius=0.0):

        Entity.__init__(self, x_pos=x_pos, y_pos=y_pos,
                        length=radius, width=radius,
                        parent=parent, children=children)

        self.radius = radius

    def __str__(self):
        return "<Patch x:%s y:%s r:%s n:%s>" % (
            self.x_pos, self.y_pos, self.radius, len(self.entities))

    def radius(self, radius=None):
        if radius is not None:
            self.radius = radius

        return self.radius

    def add_entity(self, entity=None):
        '''
        Add an entity to a random position in patch
        '''
        if entity is None:
            entity = Entity(parent=self)

        if entity.x_pos == 0.0 and entity.y_pos == 0.0:
            entity.x_pos, entity.y_pos = self.rnd_patch_position()

        self.add_child(entity)

        return entity

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
