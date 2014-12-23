import sys
from animate import Animate


class Searcher(Animate):
    '''
    Simple searcher that has a concept of time and encounters
    '''
    MAX_TIME_SINCE_ENC = sys.maxint

    def __init__(self,
                 start_direction=0.0,
                 max_speed=1.0,
                 max_turn=30.0,
                 probability_positive_turn=0.5,
                 start_x=0.0,
                 start_y=0.0):
        # super(Searcher, self).__init__(
        Animate.__init__(
            self,
            start_direction,
            max_speed,
            max_turn,
            probability_positive_turn,
            start_x,
            start_y)
        self.giving_up_time = 0
        self.time_since_encounter = Searcher.MAX_TIME_SINCE_ENC
