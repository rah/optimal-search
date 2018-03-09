class Entity(object):
    '''
    An entity has:
      - position(x,y)
      - size(length, width)
      - energy
    An entity may have a parent entity
    An entity may have child entities
    '''

    def __init__(
            self,
            energy=0.0,
            x_pos=0.0,
            y_pos=0.0,
            length=0.0,
            width=0.0,
            parent=None,
            children=None):
        self.energy = energy
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.length = length
        self.width = width
        self.parent = parent
        if children is None:
            self.children = []
        else:
            self.children = children

    def add_child(self, entity):
        self.children.append(entity)

    def remove_child(self, entity):
        self.children.remove(entity)

    def remove_self(self):
        if self.parent is not None:
            self.parent.children.remove(self)

    def total_energy(self):
        '''
        returns the sum of all energy
        '''
        total_energy = self.energy
        for child in self.children:
            total_energy += child.energy

        return total_energy

    def set_bounds(self, x, y):
        '''
        Ensure that x, y are within the bounds of this entity.
        Reset x,y so that a torus is formed
        '''
        if x < 0.0:
            x = self.length
        if x > self.length:
            x = 0.0

        if y < 0.0:
            y = self.width
        if y > self.width:
            y = 0.0

        return x, y
