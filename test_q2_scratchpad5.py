from unittest.mock import patch
from unittest import TestCase
from q2_scratchpad5 import answer

class Test(TestCase):

    # get_input will return 'yes' during this test
    @patch('yourmodule.get_input', return_value='yes')
    def test_answer_yes(self, input):
        self.assertEqual(answer(), 'you entered yes')

    @patch('yourmodule.get_input', return_value='no')
    def test_answer_no(self, input):
        self.assertEqual(answer(), 'you entered no')