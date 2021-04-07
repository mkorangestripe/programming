#!/usr/bin/env python
# Estimating the square root of 'x'
# This is an example of successive approximation using the
# guess-and-check method (exhaustive enumeration) and the bisection method.
# With larger numbers like 2500, the number of guesses is less than half
# than without using the bisection method.
# Examples from MIT OCW


# Simple guess-and-check
x = 2500
numGuesses = 0
upper = int(x / 2)
for i in range(0, upper):
    numGuesses += 1
    if i**2 == x:
        print('numGuesses =', numGuesses)
        break

# numGuesses = 51


# Successive approximation using guess-and-check and bisection methods.
# For 'x = 2500', numGuesses = 20
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(x, 1)
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon and ans <= x:
    print(low, high, ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0

print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)

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
# numGuesses = 13
# 5.00030517578 is close to square root of 25
