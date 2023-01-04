""" Extracts text between marker lines. """

import argparse
import fileinput
import sys
import typing

def extract(lines:list[str], start_marker:int, end_marker:int)->list[str]:
    """
    Finds lines that lie between a start and end marker.

    Raises
    ------
    ValueError: invalid formatting
    """
    out_lines = []
    is_scan_mode = True
    for line_no, line in enumerate(lines):
        if is_scan_mode:
            if start_marker in line:
                is_scan_mode = False
            elif end_marker in line:
                msg_error(line_no)
        else:
            if end_marker in line:
                is_scan_mode = True
            elif start_marker in line:
                msg_error(line_no)
            else:
                out_lines.append(line)
    if not is_scan_mode:
        msg_error(line_no)
    return out_lines

def msg_error(num):
     raise ValueError("*** Matching error on line %d:" % num)

# Handline command line options
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog = 'grep-lline',
                    description = 'Extracts text between start and end markers in stdin. Writes to stdout.')
    parser.add_argument('source_file', type=open, help="Source file to process.")
    #parser.add_argument('source_file', help="Source file to process.")
    parser.add_argument('-s', '--start_marker', help="Marker to start collecting lines")      # Staring for starting marker
    parser.add_argument('-e', '--end_marker', help="Marker to stop collecting lines")      # Staring for ending marker
    args = parser.parse_args()
    in_lines = [l.strip() for l in args.source_file.readlines()]
    out_lines = extract(in_lines, args.start_marker, args.end_marker)
    out_text = "\n".join(out_lines)
    sys.stdout.write(out_text)