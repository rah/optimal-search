import random

from src.simulation.entity import Entity
from src.simulation.patch import Patch


class Environment(Entity):
    '''
    An environment is an Entity that contains:
    - a set of patches
    - one searcher
    '''

    def __init__(self, p):
        Entity.__init__(self, p)
        self.length = p.getint('ENVIRONMENT', 'length')
        self.width = p.getint('ENVIRONMENT', 'width')
        self.max_patch_radius_ratio = p.getfloat(
            'ENVIRONMENT', 'max_patch_radius_ratio')

        self.create_patches()

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
            patch = Patch(self.p, parent=self)

        if patch.parent is None:
            patch.parent = self

        # set the size of the patch
        # TODO: Allow for instance parent max ratio
        if patch.radius is None or patch.radius == 0.0:
            patch.radius = random.random() * (
                self.width * self.max_patch_radius_ratio)

        # set the location of the patch
        if (
                patch.x_pos is None or patch.y_pos is None or
                patch.x_pos == 0.0 or patch.y_pos == 0.0
        ):
            patch.x_pos, patch.y_pos = self.patch_location(patch.radius)

        self.children.append(patch)
        return patch

    def patch_location(self, radius):
        '''
        Returns a random set of coordinates within the environment
        boundaries.

        TODO: Account for the patch radius
              Create different types of distributions
        '''
        x = self.length * random.random()
        y = self.width * random.random()

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

    def create_patches(self):
        for i in range(self.p.getint('ENVIRONMENT', 'n_patches')):
            self.add_patch().create_entities(
                random.randint(
                    self.p.getint('PATCH', 'min_entities_per_patch'),
                    self.p.getint('PATCH', 'max_entities_per_patch')))
