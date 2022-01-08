import unittest
from context import src
from context import config


class TestPatch(unittest.TestCase):

    def setUp(self):
        self.patch = src.simulation.patch.Patch(config)

    def test_instance(self):
        self.assertIsNotNone(self.patch)
        self.assertTrue(self.patch.x_pos == 0.0)
        self.assertTrue(self.patch.y_pos == 0.0)
        self.assertTrue(self.patch.radius == 0.0)
        self.assertTrue(len(self.patch.children) == 0)

    def test_add_entity_when_entity_is_none(self):
        self.patch.x_pos = 10.0
        self.patch.y_pos = 10.0
        self.patch.radius = 1.0

        self.patch.add_entity()
        self.assertTrue(len(self.patch.children) > 0)

        entity = self.patch.children[0]
        self.assertTrue(
            entity.x_pos != 0.0 and
            entity.y_pos != 0.0
        )
        self.patch.remove_child(entity)

    def test_create_entities(self):
        self.patch.create_entities(10)
        self.assertTrue(len(self.patch.children) == 10)
