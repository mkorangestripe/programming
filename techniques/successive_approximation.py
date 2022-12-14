#!/usr/bin/env python

"""
Estimating the square root of 'x'
This is an example of successive approximation using the
guess-and-check method (exhaustive enumeration) and the bisection method.
With larger numbers like 2500, the number of guesses is less than half
than without using the bisection method.
Examples from MIT OCW
"""

# Simple guess-and-check
X = 2500
NUM_GUESSES = 0
UPPER = X//2
for i in range(0, UPPER):
    NUM_GUESSES += 1
    if i**2 == X:
        print('NUM_GUESSES =', NUM_GUESSES)
        break

# NUM_GUESSES = 51


# Successive approximation using guess-and-check and bisection methods.
# For 'X = 2500', NUM_GUESSES = 20
X = 25
EPSILON = 0.01
NUM_GUESSES = 0
LOW = 0.0
high = max(X, 1)
ans = (high + LOW)/2.0

while abs(ans**2 - X) >= EPSILON and ans <= X:
    print(LOW, high, ans)
    NUM_GUESSES += 1
    if ans**2 < X:
        LOW = ans
    else:
        high = ans
    ans = (high + LOW)/2.0

print('NUM_GUESSES =', NUM_GUESSES)
print(ans, 'is close to square root of', X)

# 0.0 25 12.5
# 0.0 12.5 6.25
# 0.0 6.25 3.125
# 3.125 6.25 4.6875
# 4.6875 6.25 5.46875
# 4.6875 5.46875 5.078125
# 4.6875 5.078125 4.8828125
# 4.8828125 5.078125 4.98046875
# 4.98046875 5.078125 5.029296875
# 4.98046875 5.029296875 5.0048828125
# 4.98046875 5.0048828125 4.99267578125
# 4.99267578125 5.0048828125 4.99877929688
# 4.99877929688 5.0048828125 5.00183105469
# NUM_GUESSES = 13
# 5.00030517578 is close to square root of 25
