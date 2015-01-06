import unittest
import searcher


class TestSearcher(unittest.TestCase):

    def setUp(self):
        self.mover = searcher.Searcher()

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

        self.assertTrue(self.mover.giving_up_time == 0)
        self.assertTrue(
            self.mover.time_since_encounter ==
            searcher.Searcher.MAX_TIME_SINCE_ENC)
