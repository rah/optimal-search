class Entity(object):
    '''
    An entity has a position
    '''

    def __init__(
            self,
            energy=0.0,
            x_pos=0.0,
            y_pos=0.0):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def setx(self, x):
        self.curr_x = x
        self.X[len(self.X) - 1] = x

    def sety(self, y):
        self.curr_y = y
        self.Y[len(self.Y) - 1] = y
