from random import random
from patch import Patch


class Environment(object):
    '''
    An environment contains a set of patches
    '''

    # In calculating the radius of a patch this constraint can be used
    MAX_PATCH_RADIUS_RATIO = 0.01

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
        return "<Environment length:%s width:%s patches:%s>" % (
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

        # check the radius to make sure the patch is within the environment
        if (x - radius) <= 0.0:
            x = x + abs(x - radius)

        if (x + radius) >= self.length:
            x = x - (x + radius - self.length)

        # TODO: y
        if (y - radius) <= self.width:
            y = y + abs(y - radius)

        if (y + radius) >= self.width:
            y = y - (y + radius - self.width)

        return x, y

    def create_patches(self, n_patches=None):
        if n_patches is not None:
            self.n_patches = n_patches

        for i in range(self.n_patches):
            self.add_patch()
