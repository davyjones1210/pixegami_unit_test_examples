import unittest
from unittest.mock import patch
from io import StringIO
from q2_scratchpad4 import yes_or_no

class TestYesOrNo(unittest.TestCase):
    @patch('builtins.input', return_value="yes")
    def test_yes_answer(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            yes_or_no()
            self.assertEqual(mock_stdout.getvalue().strip(), "Quitter!")

    @patch('builtins.input', return_value="no")
    def test_no_answer(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            yes_or_no()
            self.assertEqual(mock_stdout.getvalue().strip(), "Awesome!")

    @patch('builtins.input', return_value="maybe")
    def test_invalid_answer(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            yes_or_no()
            self.assertEqual(mock_stdout.getvalue().strip(), "BANG!")

if __name__ == "__main__":
    unittest.main()