# import re
# test_text = re.findall('#+|\.+','##.....##.########.##.....##.')
# test_text2 = re.findall('#+|\.+','.#######..##..........###....')
# print(test_text)
# print(test_text2)

# from unittest.mock import patch, call
#
# @patch('builtins.print')
# def test_print(mocked_print):
#     print('foo')
#     print()
#
#     assert mocked_print.mock_calls == [call('foo'), call()]

def f(integer):  # defined in and imported from separate module
    if isinstance(integer, str):
        print("WARNING: integer is str")

import builtins
import contextlib, io
from unittest.mock import Mock


def test_f():
    mock = Mock()
    mock.side_effect = print  # ensure actual print is called to capture its txt
    print_original = print
    builtins.print = mock

    try:
        str_io = io.StringIO()
        with contextlib.redirect_stdout(str_io):
            f("5")
        output = str_io.getvalue()

        assert print.called  # `called` is a Mock attribute
        assert output.startswith("WARNING:")
    finally:
        builtins.print = print_original  # ensure print is "unmocked"