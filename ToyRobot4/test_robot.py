import unittest
from unittest.mock import patch
from io import StringIO
import robot


class MyTestCase(unittest.TestCase):
    
    @patch("sys.stdin", StringIO("forward 10\nforward 5\nreplay"))
    def test_replay(self):
        self.assertEqual(robot.do_replay('BOB', '2'), (True, ' > BOB replayed 0 commands.'))

if __name__ == '__main__':
    unittest.main()