#!/usr/bin/python3

import shutil
import argparse


if __name__ == '__main__':
  parser = argparse.ArgumentParser(
      description='Finds path for an executeable.')
  parser.add_argument('command', 
      type=str, 
      help='Command to search for')
  args = parser.parse_args()
  print (shutil.which(args.command))
