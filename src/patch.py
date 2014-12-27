from entity import Entity


class Patch(Entity):
    '''
    A patch contains a set of entities
    '''

    def __init__(
            self,
            x_pos=0.0,
            y_pos=0.0,
            radius=0.0,
            n_entity=0):

        Entity.__init__(self, x_pos, y_pos)

        self.radius = radius
        self.n_entity = n_entity

    def __str__(self):
        return "<Patch x:%s y:%s r:%s n:%s>" % (
            self.x_pos, self.y_pos, self.radius, self.n_entity)

    def add_entity(self, entity=None):
        pass
