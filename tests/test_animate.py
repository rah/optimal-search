import unittest
from context import src
from context import config


class TestAnimate(unittest.TestCase):

    def setUp(self):
        self.mover = src.simulation.animate.Animate(config)

    def test_instance(self):
        self.assertIsNotNone(self.mover)
        self.assertTrue(self.mover.direction == 0.0)
        self.assertTrue(self.mover.max_speed == 1.0)
        self.assertTrue(self.mover.average_turn == 20.0)
        self.assertTrue(self.mover.turn_std_dev == 5.0)
        self.assertTrue(self.mover.positive_turn == 0.5)
        self.assertTrue(self.mover.curr_x == 0.0)
        self.assertTrue(self.mover.curr_y == 0.0)
        self.assertIsNotNone(self.mover.X)
        self.assertIsNotNone(self.mover.Y)
        self.assertIsNotNone(self.mover.A)

    def test_move(self):
        x, y, a = self.mover.get_movement()
        xlen1 = len(x)
        self.assertTrue(xlen1 > 0)

        self.mover.move()

        x, y, a = self.mover.get_movement()
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

    def test_angle_turned(self):
        turn = self.mover.angle_turned()
        self.assertTrue(
            abs(turn) <= self.mover.average_turn * (3 * self.mover.turn_std_dev)
            and
            abs(turn) <= self.mover.average_turn * (3 * self.mover.turn_std_dev)
        )

    def test_distance_moved(self):
        dist_moved = self.mover.distance_moved(self.mover.max_speed)
        self.assertTrue(dist_moved <= self.mover.max_speed)
