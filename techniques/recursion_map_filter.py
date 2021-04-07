#!/usr/bin/env python
# Recursion
# Also see recursive prime number generator examples

# Converting an iterative map function to recursive
# These return cubes [1, 8, 27]

l1 = [1,2,3]

def cube(x):
    return x*x*x

def map_iter(f,lx):
    cubes = []
    for i in lx:
        cubes.append(f(i))
    return cubes

cubes = []
def map_recur(f,lx):
    if len(lx) != 0:
        i, lx = lx[0], lx[1:]
        cubes.append(f(i))
        map_recur(f, lx)
    return cubes

# As a list comprehension
[cube(i) for i in l1]


# Converting an iterative filter function to recursive
# These return numbers not divisible by 2 or 3
# [5, 7, 11, 13, 17, 19, 23]

l1 = range(2, 25)

def check_remainder(x):
    return x % 2 != 0 and x % 3 != 0

def filter_iter(f,lx):
    no_remainder = []
    for i in lx:
        if f(i):
            no_remainder.append(i)
    return no_remainder

no_remainders = []
def filter_recur(f,lx):
    if len(lx) != 0:
        i, lx = lx[0], lx[1:]
        if f(i):
            no_remainders.append(i)
        filter_recur(f, lx)
    return no_remainders

# As a list comprehension
[i for i in l1 if check_remainder(i)]
