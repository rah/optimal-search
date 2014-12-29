import unittest
import patch


class TestPatch(unittest.TestCase):

    def setUp(self):
        self.patch = patch.Patch()

    def test_instance(self):
        self.assertIsNotNone(self.patch)
        self.assertTrue(self.patch.x_pos == 0.0)
        self.assertTrue(self.patch.y_pos == 0.0)
        self.assertTrue(self.patch.radius == 0.0)
        self.assertTrue(len(self.patch.entities) == 0)

    def test_add_entity_when_entity_is_none(self):
        self.patch.x_pos = 10.0
        self.patch.y_pos = 10.0
        self.patch.radius = 1.0

        self.patch.add_entity()
        self.assertTrue(len(self.patch.entities) > 0)

        entity = self.patch.entities[0]
        self.assertTrue(
            entity.x_pos <= self.patch.x_pos + self.patch.radius and
            entity.x_pos >= self.patch.x_pos - self.patch.radius
        )
        self.assertTrue(
            entity.y_pos <= self.patch.y_pos + self.patch.radius and
            entity.y_pos >= self.patch.y_pos - self.patch.radius
        )

    def test_create_entities(self):
        self.patch.create_entities(10)
        self.assertTrue(len(self.patch.entities) == 10)
