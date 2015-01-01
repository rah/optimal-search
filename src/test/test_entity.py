import unittest
import entity


class TestEntity(unittest.TestCase):

    def setUp(self):
        self.entity = entity.Entity()

    def test_instance(self):
        self.assertIsNotNone(self.entity)
        self.assertTrue(self.entity.energy == 0.0)
        self.assertTrue(self.entity.x_pos == 0.0)
        self.assertTrue(self.entity.y_pos == 0.0)
        self.assertTrue(self.entity.length == 0.0)
        self.assertTrue(self.entity.width == 0.0)
        self.assertTrue(len(self.entity.parent) == 0)
        self.assertTrue(len(self.entity.children) == 0)

    def test_energy_no_children(self):
        self.assertTrue(self.entity.total_energy() == 0.0)

    def test_energy_one_child(self):
        child = entity.Entity()
        child.energy = 1.0
        self.entity.add(child)
        self.assertTrue(self.entity.total_energy() == 1.0)
        self.entity.remove(child)
        self.assertTrue(self.entity.total_energy() == 0.0)

    def test_energy_two_children(self):
        c1 = entity.Entity(energy=1.0)
        c2 = entity.Entity(energy=1.0)
        self.entity.add(c1)
        self.entity.add(c2)
        self.assertTrue(self.entity.total_energy() == 2.0)
        self.entity.remove(c1)
        self.entity.remove(c2)
        self.assertTrue(self.entity.total_energy() == 0.0)

    def test_bounds(self):
        x = -0.1
        y = -0.1
        x, y = self.entity.set_bounds(x, y)
        self.assertTrue(x == 0.0 and y == 0.0)

        x = 0.1
        y = 0.1
        x, y = self.entity.set_bounds(x, y)
        self.assertTrue(x == 0.0 and y == 0.0)
