import unittest
from context import src
from context import config


class TestEnvironment(unittest.TestCase):

    def setUp(self):
        self.env = src.simulation.environment.Environment(config)

    def test_instance(self):
        self.assertIsNotNone(self.env)

    def test_add_patch(self):
        self.env.add_patch()
        self.assertIsNotNone(self.env.children)
        self.assertTrue(len(self.env.children) > 0)
        self.assertIsNotNone(self.env.children[0])

    def test_patch_location(self):
        for i in range(100):
            x, y = self.env.patch_location(10.0)
            self.assertTrue((x >= 0.0) and (x <= self.env.length))
            self.assertTrue(y >= 0.0 and y <= self.env.width)

    def test_create_patches(self):
        self.env.children = []
        self.env.create_patches()
        self.assertGreaterEqual(len(self.env.children), config.getint("ENVIRONMENT", "min_patches"))
        self.assertLessEqual(len(self.env.children), config.getint("ENVIRONMENT", "max_patches"))
