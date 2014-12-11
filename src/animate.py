import random
from math import cos, sin, radians


class Animate:

    def __init__(self):
        # basic attributes
        self.direction = 0.0
        self.speed = 1.0

        # Memory of places visited
        self.X = []
        self.Y = []

        self.curr_x = 0.0
        self.curr_y = 0.0

        self.X.append(self.curr_x)
        self.Y.append(self.curr_y)

    def move(self):
        self.set_direction(self.angle_turned())
        distance = self.distance_moved(self.speed)

        x, y = self.relMove(self.direction, distance)
        self.curr_x += x
        self.curr_y += y

        self.X.append(self.curr_x)
        self.Y.append(self.curr_y)

    def relMove(self, direction, distance):
        '''
        return the relative x, y coordinates give direction and distance
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
        max_turn = 30.0
        turn = max_turn * random.random()

        if random.random() > 0.5:
            return -(turn)
        else:
            return turn

    def distance_moved(self, speed):
        return random.random() * speed

    def get_movement(self):
        return self.X, self.Y
