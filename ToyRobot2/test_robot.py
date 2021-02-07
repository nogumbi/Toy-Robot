import unittest
from io import StringIO
from unittest.mock import patch
import robot

class MyTestCase(unittest.TestCase):
    
    @patch('sys.stdin', StringIO('ofF\noff\nOfF'))
    def test_command_list(self):
        name = 'BOB'
        command = robot.get_command_input(name)
        if command == 'OFF':
            self.assertEqual(command, 'OFF')
        elif command == 'HELP':
            self.assertEqual(command, 'HELP')
        elif command == 'FORWARD':
            self.assertEqual(command, 'FORWARD')
        elif command == 'BACK':
            self.assertEqual(command, 'BACK')
        elif command == 'RIGHT':
            self.assertEqual(command, 'RIGHT')
        elif command == 'LEFT':
            self.assertEqual(command, 'LEFT')
        elif command == 'SPRINT':
            self.assertEqual(command, 'SPRINT')
        
    def test_limit_area(self):
        name = 'BOB'
        coordinates = {
            'x' : 0,
            'y' : 0
        }
        check = robot.limited_area(name, coordinates)
        self.assertEqual(check, True)

if __name__ == '__main__':
    unittest.main()
