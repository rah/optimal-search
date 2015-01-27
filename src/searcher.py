import sys
import random
from math import hypot
from animate import Animate


class Searcher(Animate):
    '''
    Simple searcher that has a concept of time and encounters
    '''
    MAX_TIME_SINCE_ENC = sys.maxint
    SPEED_DETECTION_RATIO = 10.0

    def __init__(self,
                 max_speed=1.0,
                 average_turn=20.0,
                 turn_std_dev=5.0,
                 probability_positive_turn=0.5,
                 x_pos=0.0,
                 y_pos=0.0,
                 parent=None):
        # super(Searcher, self).__init__(
        Animate.__init__(
            self,
            max_speed,
            average_turn,
            turn_std_dev,
            probability_positive_turn,
            x_pos,
            y_pos,
            parent=parent)
        self.captured = []
        self.giving_up_time = 0
        self.time_since_encounter = Searcher.MAX_TIME_SINCE_ENC
        self.time_since_capture = Searcher.MAX_TIME_SINCE_ENC
        self.detection_range = max_speed * Searcher.SPEED_DETECTION_RATIO

    def move(self):
        self.time_since_capture += 1
        self.time_since_encounter += 1
        super(Searcher, self).move()

    def detect(self):
        entity_detected = self.is_entity_in_detection_range()
        if entity_detected is not None:
            self.time_since_encounter = 0

        return entity_detected

    def capture(self, entity):
        '''
        Determines whether the searcher captures the entity or not

        TODO: Initial implementation just a random decision 50/50
              Need to work out what this should be
        '''
        if entity is not None:
            if random.random() > 0.5:
                self.time_since_capture = 0
                self.captured.append(entity)
                entity.remove_self()  # remove from patch

    def is_entity_in_detection_range(self):
        '''
        Determines if an entity is within detection range.

        To avoid having to check every entity, only check for entities within a
        patch if within a patch.
        '''
        entity_found = None
        in_patch = self.is_in_patch()
        if in_patch is not None:
            for entity in in_patch.children:
                if hypot(
                        self.curr_x - entity.x_pos,
                        self.curr_y - entity.y_pos
                ) <= self.detection_range:
                    entity_found = entity
                    break

        return entity_found

    def is_in_patch(self):
        patch_found = None
        for patch in self.parent.children:
            if hypot(
                    self.curr_x - patch.x_pos,
                    self.curr_y - patch.y_pos
            ) <= patch.radius:
                patch_found = patch
                break

        return patch_found

