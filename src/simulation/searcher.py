import sys
from math import hypot

from src.simulation.animate import Animate


class Searcher(Animate):
    '''
    Simple searcher that has a concept of time and encounters
    '''
    MAX_TIME_SINCE_ENC = sys.maxsize # set to an arbitary large number

    def __init__(self, p, parent=None):
        # super(Searcher, self).__init__(
        Animate.__init__(self, p, parent=parent)

        self.giving_up_time = p.getint("SEARCHER", "giving_up_time")
        self.speed_detection_ratio = p.getfloat("SEARCHER", "speed_detection_ratio")

        self.time_since_encounter = Searcher.MAX_TIME_SINCE_ENC
        self.detection_range = self.max_speed * self.speed_detection_ratio

    def move(self):
        self.time_since_encounter += 1
        super(Searcher, self).move()

    def detect(self):
        entity_detected = self.is_entity_in_detection_range()
        if entity_detected is not None:
            self.time_since_encounter = 0

        return entity_detected

    def is_entity_in_detection_range(self):
        '''
        Determines if an entity is within detection range.
        To avoid having to check every entity, only check for 
        entities within a patch if within a patch.

        Returns the entity if detected or None
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
        '''
        Determines if the searcher is in a patch:
            If the euclidean distance of the searcher from the centre of the patch 
            is less than the radius of the patch then
                returns the patch otherwise None
        '''
        patch_found = None
        for patch in self.parent.children:
            if hypot(
                    self.curr_x - patch.x_pos,
                    self.curr_y - patch.y_pos
            ) <= patch.radius:
                patch_found = patch
                break
        return patch_found
