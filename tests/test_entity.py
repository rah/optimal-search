import unittest
from context import src
from context import config


class TestEntity(unittest.TestCase):

    def setUp(self):
        self.entity = src.simulation.entity.Entity(config)

    def test_instance(self):
        self.assertIsNotNone(self.entity)
        self.assertTrue(self.entity.energy == 0.0)
        self.assertTrue(self.entity.x_pos == 0.0)
        self.assertTrue(self.entity.y_pos == 0.0)
        self.assertTrue(self.entity.length == 1.0)
        self.assertTrue(self.entity.width == 1.0)
        self.assertTrue(self.entity.parent is None)
        self.assertTrue(len(self.entity.children) == 0)

    def test_energy_no_children(self):
        self.assertTrue(self.entity.total_energy() == 0.0)

    def test_energy_one_child(self):
        child = src.simulation.entity.Entity(config)
        child.energy = 1.0
        self.entity.add_child(child)
        self.assertTrue(self.entity.total_energy() == 1.0)
        self.entity.remove_child(child)
        self.assertTrue(self.entity.total_energy() == 0.0)

    def test_energy_two_children(self):
        c1 = src.simulation.entity.Entity(config)
        c2 = src.simulation.entity.Entity(config)
        c1.energy = 1.0
        c2.energy = 1.0
        self.entity.add_child(c1)
        self.entity.add_child(c2)
        self.assertTrue(self.entity.total_energy() == 2.0)
        self.entity.remove_child(c1)
        self.entity.remove_child(c2)
        self.assertTrue(self.entity.total_energy() == 0.0)

    def test_bounds(self):
        x = -0.1
        y = -0.1
        x, y = self.entity.set_bounds(x, y)
        self.assertTrue(x == 1 and y == 1)

        x = 1.1
        y = 1.1
        x, y = self.entity.set_bounds(x, y)
        self.assertTrue(x == 0.0 and y == 0.0)
