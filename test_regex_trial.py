import io
import sys


def foo(inStr):
    print("hi")


def test_foo():
    capturedOutput = io.StringIO()  # Create StringIO.
    sys.stdout = capturedOutput  # Redirect stdout.
    try:
        foo('test')  # Call function.
    except:
        sys.stdout = sys.__stdout__  # Reset redirect.
        raise
    sys.stdout = sys.__stdout__  # Reset redirect.
    print('Captured', capturedOutput.getvalue())  # Now works.

    test_foo()