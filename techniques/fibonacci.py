#!/usr/bin/env python

"""
Fibonacci sequence using memoization
The first two numbers in the Fibonacci sequence are either 1 and 1, or 0 and 1...
depending on the chosen starting point of the sequence,
and each subsequent number is the sum of the previous two.
By using the memo, the order of growth drops from 2^n to n^2 ???
"""

memo0 = {0:0, 1:1}  # 0, 1, 1, 2, 3, 5, 8, 13, 21
memo1 = {0:1, 1:1}  # 1, 1, 2, 3, 5, 8, 13, 21

def fibonacci(n, memo):
    """Return next nth number in the Fibonacci sequence"""
    if not n in memo:
        memo[n] = fibonacci(n-1, MEMO) + fibonacci(n-2, MEMO)
    return memo[n]

FIB_NUM = 8
MEMO = memo0
fibonacci(FIB_NUM, MEMO)
print(MEMO[FIB_NUM - 1])

# The Golden Ratio
# Line segment of segments 'a' and 'b' where a+b is to 'a' as 'a' is to 'b'.
# The ration is about 1.618.
# The higher the numbers in the Fibonacci sequence, the closer their ratio to the Golden ratio.
# The Greek letter φ (phi) is used to symbolize the golden ratio.
# If a Fibonacci number is divided by its immediate predecessor in the sequence, the quotient approximates φ.
# These approximations are alternately lower and higher than φ, and converge on φ as the Fibonacci numbers increase.
# The golden spiral is a logarithmic spiral whose growth factor is φ, the golden ratio.
