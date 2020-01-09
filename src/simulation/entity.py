class Entity(object):
    '''
    An entity has:
      - energy
      - position(x,y)
      - size(length, width)
      - energy
    An entity may have a parent entity
    An entity may have child entities
    '''

    def __init__(
            self,
            p,
            parent=None,
            children=None):
        self.p = p
        self.energy = p.getfloat("ENTITY", "energy")
        self.x_pos = p.getfloat("ENTITY", "x_pos")
        self.y_pos = p.getfloat("ENTITY", "y_pos")
        self.length = p.getint("ENTITY", "length")
        self.width = p.getint("ENTITY", "width")
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

    def number_children(self):
        if self.children:
            return len(self.children)
        else:
            return 0

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
