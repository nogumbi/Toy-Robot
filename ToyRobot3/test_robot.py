import unittest
from unittest.mock import patch
from io import StringIO
import robot


class MyTestCase(unittest.TestCase):
    
    @patch("sys.stdin", StringIO("forward 10\nforward 5\nreplay"))
    def test_replay(self):
        self.assertEqual(robot.do_replay('BOB', '2'), (True, ' > BOB replayed 0 commands.'))

    @patch("sys.stdin", StringIO("forward\nforward 5\nreplay silent"))
    def test_replay_silent(self):
        self.assertEqual(robot.replay_silent('BOB'), (True, ' > BOB replayed 0 commands silently.'))
    
    @patch("sys.stdin", StringIO("forward 10\nback 5\nreplay reversed"))
    def test_replay_reversed(self):
        self.assertEqual(robot.replay_reversed('BOB'),(True, ' > BOB replayed 0 commands in reverse.'))
    
    @patch("sys.stdin", StringIO("forward 10\nright\nreplay reversed silent"))
    def test_replay_silent_reversed(self):
        self.assertEqual(robot.silent_reverse('BOB'), (True, ' > BOB replayed 0 commands in reverse silently.'))

if __name__ == '__main__':
    unittest.main()
