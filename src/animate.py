import random
from math import cos, sin, radians


class Animate(object):
    '''
    A simple entity that can move around randomly
    '''
    def __init__(
            self,
            start_direction=0.0,
            max_speed=1.0,
            max_turn=30.0,
            probability_positive_turn=0.5,
            start_x=0.0,
            start_y=0.0
    ):
        # basic attributes
        self.direction = start_direction
        self.max_speed = max_speed
        self.max_turn = max_turn
        self.positive_turn = probability_positive_turn

        self.curr_x = start_x
        self.curr_y = start_y

        # Memory of places visited
        self.X = []
        self.Y = []
        self.X.append(self.curr_x)
        self.Y.append(self.curr_y)

    def move(self):
        self.set_direction(self.angle_turned())
        distance = self.distance_moved(self.max_speed)

        x, y = self.relMove(self.direction, distance)
        self.curr_x += x
        self.curr_y += y

        self.X.append(self.curr_x)
        self.Y.append(self.curr_y)

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
