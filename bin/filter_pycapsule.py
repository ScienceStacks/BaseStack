#!/usr/bin/python3
"""Filters Pycapsule error"""

import fileinput
import sys

STRING = "RuntimeError: Object of type <class 'NamedArray'>"
NUM_AFTER = 5  # How many lines after to delete
NUM_BEFORE = 4  # How far before to delete

output_lines = []
delete_count = 0
for line in fileinput.input():
    if delete_count > 0:
        delete_count -= 1
    elif STRING in line:
        output_lines = output_lines[:-NUM_BEFORE]
        delete_count = NUM_AFTER
    else:
        output_lines.append(line)
#
output_str = "\n".join(output_lines)
sys.stdout.write(output_str)
