class Entity(object):
    '''
    An entity that has a position and energy
    '''

    def __init__(
            self,
            energy=0.0,
            x_pos=0.0,
            y_pos=0.0):
        self.energy = energy
        self.x_pos = x_pos
        self.y_pos = y_pos
