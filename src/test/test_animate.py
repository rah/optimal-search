import unittest
import animate


class TestAnimate(unittest.TestCase):

    def setUp(self):
        self.mover = animate.Animate()

    def test_instance(self):
        self.assertIsNotNone(self.mover)
        self.assertTrue(self.mover.direction == 0)

    def test_move(self):
        x, y = self.mover.get_movement()
        xlen1 = len(x)
        self.assertTrue(xlen1 > 0)

        self.mover.move()

        x, y = self.mover.get_movement()
        xlen2 = len(x)
        self.assertTrue(xlen2 > xlen1)

        self.assertTrue(x[xlen1-1] != x[xlen2-1])

    def test_rel_move(self):
        speed = 1.0
        direction = 0.0

        x, y = self.mover.relMove(direction, speed)
        self.assertEqual(x, 1.0)
        self.assertEqual(y, 0.0)

    def test_set_direction(self):
        self.mover.direction = 0.0
        self.assertEqual(self.mover.direction, 0.0)

        self.mover.set_direction(30.0)
        self.assertEqual(self.mover.direction, 30.0)
