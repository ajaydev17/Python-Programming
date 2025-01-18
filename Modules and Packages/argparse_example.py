"""
argparse is a Python module for creating CLIs by parsing command-line arguments. You can
specify different arguments, their types, default values, and help messages. This module is
ideal for creating interactive scripts with flexible command-line options.
"""

import argparse

# initialize the parser
parser = argparse.ArgumentParser(description='A simple calculator')
parser.add_argument('num1', type=float, help='first number')
parser.add_argument('num2', type=float, help='second number')
parser.add_argument('--operation', choices=['add', 'subtract'], default='add', help='operation to perform')

# parse arguments
args = parser.parse_args()

# perform the operation
if args.operation == 'add':
    print(args.num1 + args.num2)
else:
    print(args.num1 - args.num2)

