from q2_scratchpad4 import yes_or_no
import mock


def test_quitting():

    with mock.patch('builtins.input', return_value="yes"):
        assert yes_or_no() == "Quitter!"

    with mock.patch('builtins.input', return_value="no"):
        assert yes_or_no() == "Awesome!"