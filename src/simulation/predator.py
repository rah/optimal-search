import random

from simulation.searcher import Searcher


class Predator(Searcher):
    '''
    Searches for and captures entitys
    '''

    def __init__(self, p, parent=None):
        Searcher.__init__(self, p, parent=parent)
        self.captured = []
        self.time_since_capture = Searcher.MAX_TIME_SINCE_ENC

    def capture(self, entity):
        '''
        Determines whether the predator captures the entity or not

        TODO: Initial implementation just a random decision 50/50
              Need to work out what this should be
        '''
        if entity is not None:
            if random.random() > 0.5:
                self.time_since_capture = 0
                self.captured.append(entity)
                entity.remove_self()  # remove from patch

    def move(self):
        super(Predator, self).move()

    def total_captured(self):
        return len(self.captured)
