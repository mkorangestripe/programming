#!/usr/bin/env python

"""
Prime number generators
The recursive versions below show the limits of recursion for this type of program.
"""

from math import sqrt

# This finds the last prime number before n.
N = 40 # N must be greater than 2

primelist = [2]
for i in range(3, N, 2):
    for j in range(2, i):
        if i%j == 0:
            break
        if j == int(sqrt(i)) + 1:
            primelist.append(i)
            break

print("The last prime number before", N, "is", primelist[-1])


# This finds the nth prime number.
N = 5 # N must be greater than 2

primelist = [2]
i = 3
while len(primelist) < N:
    j = 2
    while i%j != 0:
        if j == int(sqrt(i)) + 1:
            primelist.append(i)
            break
        j+=1
    i+=2

print("The", str(N) + "(st,nd,rd,th)", "prime number is", primelist[-1])
print('')


def primegen_recur(primelist, i, j, max):
    """
    Recursive version, returns list of prime numbers.
    After finding the 62nd prime, maximum recursion depth is exceeded.
    """
    if len(primelist) < max:
        if i%j != 0:
            if j == int(sqrt(i)) + 1:
                primelist.append(i)
                j=2
                i+=2
            else:
                j+=1
        else:
            j=2
            i+=2
        primegen_recur(primelist, i, j, max)
    return primelist


def primegen_recur2(primelist, i, j, max):
    """
    Same as above, but less indenting.
    Recursive version, returns list of prime numbers.
    After finding the 62nd prime, maximum recursion depth is exceeded.
    """
    if len(primelist) == max:
        return primelist
    if i%j == 0:
        j=2
        i+=2
    elif j == int(sqrt(i)) + 1:
        primelist.append(i)
        j=2
        i+=2
    else:
        j+=1
    primegen_recur2(primelist, i, j, max)
    return primelist


init_primelist = [2]
i,j = 3,2
MAX = 40

primelist = primegen_recur(init_primelist, i, j, MAX)
print(primelist)
print('')

primelist = primegen_recur2(init_primelist, i, j, MAX)
print(primelist)
