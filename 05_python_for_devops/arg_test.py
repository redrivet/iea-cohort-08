#!/usr/bin/env python3
"""
Testing for argparse for passsing in cli arguments
"""
import argparse

parser = argparse.ArgumentParser(description="Example for ArgParse-ing")

parser.add_argument("-a", action="store_true", default=False)
parser.add_argument("-b", action="store", dest="blob")
parser.add_argument("-c", action="store", dest="c")
parser.add_argument("-version", action="version", version="%(prog)s 0.1.0")

args = parser.parse_args()


# Try and run something like ./arg_test.py -a -b hello

if args.a:
    print("a was passed")
    print(args.a)
if args.blob:
    print("-b", args.blob, "was passed")
if args.c:
    print("-c", args.c, "was passed (int)")
