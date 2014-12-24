import unittest
import animate


class TestAnimate(unittest.TestCase):

    def setUp(self):
        self.mover = animate.Animate()

    def test_move(self):
        self.assertIsNotNone(self.mover)

        x, y = self.mover.get_movement()
        xlen1 = len(x)
        self.assertTrue(xlen1 > 0)

        self.mover.move()

        x, y = self.mover.get_movement()
        xlen2 = len(x)
        self.assertTrue(xlen2 > xlen1)

        self.assertTrue(x[xlen1-1] != x[xlen2-1])

    def test_rel_move(self):
        pass

    def test_set_direction(self):
        pass
