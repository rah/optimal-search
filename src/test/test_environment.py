import unittest
from environment import Environment


class TestEnvironment(unittest.TestCase):

    def setUp(self):
        self.env = Environment()

    def test_instance(self):
        self.assertIsNotNone(self.env)

    def test_add_patch(self):
        self.env.add_patch()
        self.assertIsNotNone(self.env.patches)
        self.assertTrue(len(self.env.patches) > 0)
        self.assertIsNotNone(self.env.patches[0])

    def test_patch_location(self):
        for i in range(100):
            x, y = self.env.patch_location(10.0)
            self.assertTrue((x >= 0.0) and (x <= self.env.length))
            self.assertTrue(y >= 0.0 and y <= self.env.width)

    def test_create_patches(self):
        self.env.create_patches(10)
        self.assertEqual(len(self.env.patches), 10)
