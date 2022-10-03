import argparse

parser = argparse.ArgumentParser(
    description='argparse example')

parser.add_argument('-a', action="store_true",
                    default=False)
parser.add_argument('-b', action="store", dest="blog")
parser.add_argument('-c', action="store", dest="c",
                    type=int)
parser.add_argument('--version', action='version', 
                    version='%(prog)s 2.0')

# parse args from command line, which won't work in the notebook
#args = parser.parse_args()

# $ python3 myscript.py -a -b happy
args = parser.parse_args()

print(args)

if args.a:
    print("-a was passed")
if args.blog:
    print("-b", args.blog, "was passed")
if args.c:
    print("-c", args.c, "was passed (int)")
