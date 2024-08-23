#
#
# class Fruit:
#     def __init__(self, name: str):
#         self._name = name
#
#     def get_name(self):
#         print("Getting name.")
#         return self._name
#
#     def set_name(self, new_name: str):
#         self._name = new_name
#
#
#
# if __name__ == '__main__':
#     fruit = Fruit('Banana')
#     fruit.set_name('Orange')
#     print(fruit.get_name())

# from unittest.mock import patch, call
#
# @patch('builtins.print')
# def test_print(mocked_print):
#     print('foo')
#     print()
#
#     assert mocked_print.mock_calls == [call('foo'), call()]


# python -m unittest classes_problem_q1_scratchpad.test_print

import io
import sys


def foo(inStr):
    print("hi" + inStr)



def test_foo():
    capturedOutput = io.StringIO()  # Create StringIO.
    sys.stdout = capturedOutput  # Redirect stdout.
    foo('test')  # Call function.
    sys.stdout = sys.__stdout__  # Reset redirect.
    print('Captured', capturedOutput.getvalue())  # Now works.



test_foo()

