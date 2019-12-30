from random import random

from src.simulation.entity import Entity
from src.simulation.patch import Patch


class Environment(Entity):
    '''
    An environment is an Entity that contains:
    - a set of patches
    - one searcher
    '''

    # In calculating the radius of a patch this constraint can be used
    MAX_PATCH_RADIUS_RATIO = 0.1

    def __init__(
            self,
            length=100,
            width=100,
            n_patches=0):

        Entity.__init__(self, length=length, width=width)
        self.create_patches(n_patches)

    def __str__(self):
        return "<Environment length:%s width:%s number of patches:%s>" % (
            self.length, self.width, len(self.children))

    def add_patch(self, patch=None):
        '''
        Add a patch to the environment.

        Set the location and radius of the patch in
        the environment randomly.
        '''
        if patch is None:
            # create a new empty patch
            patch = Patch(parent=self)

        if patch.parent is None:
            patch.parent = self

        # set the size of the patch
        # TODO: Allow for instance parent max ratio
        if patch.radius is None or patch.radius == 0.0:
            patch.radius = random() * (
                self.width * Environment.MAX_PATCH_RADIUS_RATIO)

        # set the location of the patch
        if (
                patch.x_pos is None or patch.y_pos is None or
                patch.x_pos == 0.0 or patch.y_pos == 0.0
        ):
            patch.x_pos, patch.y_pos = self.patch_location(patch.radius)

        self.children.append(patch)

    def patch_location(self, radius):
        '''
        Returns a random set of coordinates within the environment
        boundaries.

        TODO: Account for the patch radius
              Create different types of distributions
        '''
        x = self.length * random()
        y = self.width * random()

        x, y = self.check_radius(x, y, radius)

        return x, y

    def check_radius(self, x, y, radius):
        '''
        Check the radius to make sure the patch is within the environment,
        At this stage allow patches to overlap, so x and y are just adjusted
        '''
        if (x - radius) <= 0.0:
            x = x + abs(x - radius)

        if (x + radius) >= self.length:
            x = x - (x + radius - self.length)

        # y location
        if (y - radius) <= self.width:
            y = y + abs(y - radius)

        if (y + radius) >= self.width:
            y = y - (y + radius - self.width)

        return x, y

    def check_in_bounds(self, pos, dist, lower_bound, upper_bound):
        '''
        check that the position is within a certain dist of the bounds
        '''
        if (pos - dist) <= lower_bound:
            return True

        if (pos + dist) >= upper_bound:
            return True

        return False

    def create_patches(self, n_patches=0):
        for i in range(n_patches):
            self.add_patch()
