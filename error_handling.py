# try except statements
while True:
    try:
        x = int(raw_input("Please enter a number: "))
        break
    except ValueError:
        print "Not a valid number.  Try again..."


# try except statements with else and finally.
import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print 'cannot open', arg
    else:
        print arg, 'has', len(f.readlines()), 'lines'
        f.close()
    finally:
        print "executing finally clause"


# Raise a runtime error:
raise RuntimeError('test for validate_request_parameters debug log')


# Breakpoint Debugging with PDB
# example from linuxacademy.com
import pdb

def map(func, values):
    output_values = []
    index = 0
    while index < len(values):
        pdb.set_trace()
        output_values = func(values[index])
        index += 1
    return output_values

def add_one(val):
    return val + 1

print(map(add_one, list(range(10))))

# Run above as follows...
# python3.7 debugging.py
# pdb will break at the pbd.set_trace line and will display a (Pdb) prompt.
values
# [0, 1, 2, 3, 4]
index
# 0
output_values
# []
n
# index += 1

# Or run the file without the import line.
# This will step through line by line from the top.
# python3.7 -m pdb debugging.py
# ll
# Set a breakpoint at line 5 when index is 5
break 5, index == 5
# c

# h for help
# 'help cont' for help on cont
# q for quit
