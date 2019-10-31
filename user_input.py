# System specific parameters and functions
import sys
print sys.argv # all command line arguments.
print sys.argv[0] # the script itself.
print sys.argv[1] # first command line argument passed to the script.
sys.exit()


# Argument and options

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", type=int, choices=[0,1,2],
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2

if args.verbosity == 2:
    print "the square of {0} equals {1}".format(args.square, answer)
elif args.verbosity == 1:
    print "{0}^2 == {1}".format(args.square, answer)
else:
    print answer


# User input

# raw_input a string.
s = raw_input('Enter a number: ')
# raw_input an int.
n = int(raw_input('Enter a number: '))
type(s) # <type 'str'>
type(n) # <type 'int'>

# input() - python 2.x
# Equivalent to eval(raw_input(prompt))
# Consider using the raw_input() function for general input from users.

# Input a string.
s = str(input('Enter a number: '))
# Input an int.
n = input('Enter a number: ')
type(s) # <type 'str'>
type(n) # <type 'int'>

# input() evaluates the input.
c1 = 'sky blue'
c2 = 'brick red'
color = input('Enter a color: ')


# Signal handling

import signal
import sys

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')
signal.pause()
