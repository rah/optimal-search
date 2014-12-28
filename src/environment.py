from random import random
from patch import Patch


class Environment(object):
    '''
    An environment contains a set of patches
    '''

    # In calculating the radius of a patch this constraint can be used
    MAX_PATCH_RADIUS_RATIO = 0.1

    def __init__(
            self,
            length=100,
            width=100,
            n_patches=0):
        self.length = length
        self.width = width
        self.n_patches = n_patches
        self.patches = []

    def __str__(self):
        return "<Environment length:%s width:%s number of patches:%s>" % (
            self.length, self.width, self.n_patches)

    def add_patch(self, patch=None):
        '''
        Add a patch to the environment.

        Set the location and radius of the patch in
        the environment randomly.
        '''
        if patch is None:
            # create a new empty patch
            patch = Patch()

        # set the size of the patch
        patch.radius = random() * (
            self.width * Environment.MAX_PATCH_RADIUS_RATIO)

        # set the location of the patch
        patch.x_pos, patch.y_pos = self.patch_location(patch.radius)

        self.patches.append(patch)

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

    def check_in_bounds(pos, dist, lower_bound, upper_bound):
        '''
        check that the position is within a certain dist of the bounds
        '''
        if (pos - dist) <= lower_bound:
            return True

        if (pos + dist) >= upper_bound:
            return True

        return False

    def create_patches(self, n_patches=None):
        if n_patches is not None:
            self.n_patches = n_patches

        for i in range(self.n_patches):
            self.add_patch()
