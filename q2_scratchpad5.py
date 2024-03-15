from unittest.mock import patch
from unittest import TestCase


def get_input(text):
    return input(text)


def answer():
    ans = get_input('enter yes or no')
    if ans == 'yes':
        return 'you entered yes'
    if ans == 'no':
        return 'you entered no'

# Run from cmd prompt: python -c "from q2_scratchpad5 import *; print(answer())"

