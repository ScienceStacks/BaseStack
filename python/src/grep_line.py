""" Extracts text between marker lines. """

import argparse
import sys

def extract(lines, start_marker, end_marker):
    """
    Finds lines that lie between a start and end marker.

    Parameters
    ----------
    lines: list-str
    start_marker: str
    end_marker: str

    Returns
    -------
    list-str
    """
    out_lines = []
    is_scan_mode = True
    for line_no, line in enumerate(lines):
        if is_scan_mode:
            if start_marker in line:
                is_scan_mode = False
            elif end_marker in line:
                msg_matching_error(line_no)
        else:
            if end_marker in line:
                is_scan_mode = True
            elif start_marker in line:
                msg_matching_error(line_no)
            else:
                out_lines.append(lines)
    return out_lines

def msg_matching_error(num):
    print("*** Matching error on line %d:" % num)
    sys.exit()