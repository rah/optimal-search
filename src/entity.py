class Entity(object):
    '''
    An entity that has a position and energy
    '''

    def __init__(
            self,
            energy=0.0,
            curr_x=0.0,
            curr_y=0.0):
        self.energy = energy
        self.curr_x = curr_x
        self.curr_y = curr_y
