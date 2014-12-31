import sys
import random
from animate import Animate


class Searcher(Animate):
    '''
    Simple searcher that has a concept of time and encounters
    '''
    MAX_TIME_SINCE_ENC = sys.maxint
    SPEED_DETECTION_RATIO = 10.0

    def __init__(self,
                 start_direction=0.0,
                 max_speed=1.0,
                 max_turn=30.0,
                 probability_positive_turn=0.5,
                 x_pos=0.0,
                 y_pos=0.0):
        # super(Searcher, self).__init__(
        Animate.__init__(
            self,
            start_direction,
            max_speed,
            max_turn,
            probability_positive_turn,
            x_pos,
            y_pos)
        self.giving_up_time = 0
        self.time_since_encounter = Searcher.MAX_TIME_SINCE_ENC
        self.detection_range = max_speed * Searcher.SPEED_DETECTION_RATIO

    def capture(self, entity):
        '''
        Determines whether the searcher captures the entity or not

        Initial implementation just a random decision
        '''
        if random.random() > 0.5:
            return True
