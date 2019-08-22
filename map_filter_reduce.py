# Map
# Takes a function and a list(s) or tuple(s) as input, returns a list of results.
# Returns cubes of the numbers in the range
def cube(x):
    return x*x*x

map(cube, range(1, 11))
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# Returns sums of corresponding elements
seq = range(8)
def add(x, y):
    return x+y

map(add, seq, seq)
# [0, 2, 4, 6, 8, 10, 12, 14]


# Filter
# Takes a function and a list, tuple, or string as input, returns list of True items.
# Returns numbers not divisible by 2 or 3
def f(x):
    return x % 2 != 0 and x % 3 != 0

filter(f, range(2, 25))
# [5, 7, 11, 13, 17, 19, 23]


# Reduce
# Takes a function (with two args) and lists or tuples as input and applies
# the function cumulatively to the items of the sequence, from left to right,
# so as to reduce the sequence to a single value.

# Calls the function 'add' with the first two items in the sequence,
# then on the result and the next item, and so on.
def add(x,y):
    return x+y

reduce(add, range(1, 11))
# 55
