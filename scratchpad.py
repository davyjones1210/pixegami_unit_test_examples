from unittest.mock import Mock, patch, mock_open
import builtins
import contextlib, io
import unittest

ascii_pic = """##.....##.########.##.....##.
##.....##.##.......##.....##.
##.....##.##.......##.....##.
##.....##.######...##.....##.
##.....##.##........##...##..
##.....##.##.........##.##...
.#######..##..........###....
"""

ascii_encoded_pic = """#2.5#2.1#8.1#2.5#2.1
#2.5#2.1#2.7#2.5#2.1
#2.5#2.1#2.7#2.5#2.1
#2.5#2.1#6.3#2.5#2.1
#2.5#2.1#2.8#2.3#2.2
#2.5#2.1#2.9#2.1#2.3
.1#7.2#2.10#3.4
"""


# test_100_chars = ""
# for i in range(0, 100):
#     test_100_chars += str(i) + "\n"
test_file = ascii_encoded_pic
test_file= test_file + "999999999999999999999999999999999999999999999999999999"
print(test_file)
# # read_test_data = eight_pass.display_string_size(test_file).strip()
# print(read_test_data)