#!/usr/bin/env python
# Prime number generators
# The recursive versions below show the limits of recursion for this type of program.


# This finds the last prime number before n.
from math import sqrt
n = 40 # n must be greater than 2

primelist = [2]
for i in range(3, n, 2):
  for j in range(2, i):
    if i%j == 0:
      break
    elif j == int(sqrt(i)) + 1:
      primelist.append(i)
      break

print("The last prime number before", n, "is", primelist[-1])


# This finds the nth prime number.
from math import sqrt
n = 5 # n must be greater than 2

primelist = [2]
i = 3
while len(primelist) < n:
  j = 2
  while i%j != 0:
    if j == int(sqrt(i)) + 1:
      primelist.append(i)
      break
    else:
      j+=1
  i+=2

print("The", str(n) + "(st,nd,rd,th)", "prime number is", primelist[-1])


# Recursive version, returns list of prime numbers.
# After finding the 62nd prime, maximum recursion depth is exceeded.
from math import sqrt

def primegen(primelist, i, j, max):
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
    primegen(primelist, i, j, max)  
  return primelist


# Same as above, but less indenting.
from math import sqrt

def primegen(primelist, i, j, max):
  if len(primelist) == max:
    return primelist
  elif i%j == 0:
    j=2
    i+=2
  elif j == int(sqrt(i)) + 1:
    primelist.append(i)
    j=2
    i+=2
  else:
    j+=1
  primegen(primelist, i, j, max)
  return primelist
