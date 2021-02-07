import sys
import unittest
import world.obstacles as obstacles
import random

class MyTestCase(unittest.TestCase):
    def test_get_obstacles(self):
        self.test_get_obstacles

    def test_is_position_blocked(self):
        self.assertEqual(obstacles.is_position_blocked(0, 0), False)

    def test_is_path_blocked(self):
        self.assertEqual(obstacles.is_path_blocked(0, 0, 0, 0), False)

if __name__ == '__main__':
    unittest.main()
