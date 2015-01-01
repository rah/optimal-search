import random
from math import cos, sin, radians
from entity import Entity


class Animate(Entity):
    '''
    A simple entity that can move around
    '''

    def __init__(
            self,
            start_direction=0.0,
            max_speed=1.0,
            max_turn=30.0,
            probability_positive_turn=0.5,
            x_pos=0.0,
            y_pos=0.0,
            parent=None):

        Entity.__init__(self, x_pos=x_pos, y_pos=y_pos, parent=parent)

        # basic attributes
        self.direction = start_direction
        self.max_speed = max_speed
        self.max_turn = max_turn
        self.positive_turn = probability_positive_turn

        self.curr_x = x_pos
        self.curr_y = y_pos

        # Memory of places visited
        self.X = []
        self.Y = []
        self.X.append(self.curr_x)
        self.Y.append(self.curr_y)

    def setx(self, x):
        self.curr_x = x
        self.X.append(x)

    def sety(self, y):
        self.curr_y = y
        self.Y.append(y)

    def move(self):
        self.set_direction(self.angle_turned())
        distance = self.distance_moved(self.max_speed)

        x_rel, y_rel = self.relMove(self.direction, distance)
        x, y = self.parent.set_bounds(self.curr_x + x_rel, self.curr_y + y_rel)

        self.setx(x)
        self.sety(y)

    def relMove(self, direction, distance):
        '''
        return the relative x, y coordinates given direction and distance
        '''
        x = distance * cos(radians(float(direction)))
        y = distance * sin(radians(float(direction)))

        return x, y

    def set_direction(self, angle_turned):
        '''
        direction is 0 - 360 degrees, if the angle turned
        added to the current direction and is less than 0
        we need to reset
        '''
        self.direction += angle_turned
        if self.direction < 0.0:
            self.direction = 360.0 + self.direction
        if self.direction > 360.0:
            self.direction = self.direction - 360.0

    def angle_turned(self):
        '''
        minimal implementation, should be replaced by subclasses
        '''
        turn = self.max_turn * random.random()

        if random.random() > self.positive_turn:
            return turn
        else:
            return -(turn)

    def distance_moved(self, speed):
        '''
        minimal implementation, should be replaced by subclasses
        '''
        return random.random() * speed

    def get_movement(self):
        return self.X, self.Y
