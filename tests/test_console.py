import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        """Set up an instance of HBNBCommand for each test case"""
        self.hbnb_command = HBNBCommand()

    def test_prompt(self):
        """Test if the prompt is set correctly"""
        self.assertEqual(self.hbnb_command.prompt, '(hbnb) ')

    def test_preloop(self):
        """Test the preloop method"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.preloop()
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, '(hbnb)')

    # Add more test methods for other functionality...

    def test_do_quit(self):
        """Test the do_quit method"""
        with self.assertRaises(SystemExit):
            self.hbnb_command.do_quit(None)

    def test_do_EOF(self):
        """Test the do_EOF method"""
        with patch('builtins.print') as mock_print:
            with self.assertRaises(SystemExit):
                self.hbnb_command.do_EOF(None)
            mock_print.assert_called_once_with()

    def test_emptyline(self):
        """Test the emptyline method"""
        with patch('builtins.print') as mock_print:
            self.hbnb_command.emptyline()
            mock_print.assert_not_called()


if __name__ == '__main__':
    unittest.main()
