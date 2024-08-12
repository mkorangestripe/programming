#!/usr/bin/env python

"""
Estimating the square root of 'x'
This is an example of successive approximation using the
guess-and-check method (exhaustive enumeration) and the bisection method.
With larger numbers like 2500, the number of guesses is less than half
than without using the bisection method.
Examples from MIT OCW
"""

print("Simple guess-and-check to find square root")
X = 2500  # Number of guesses: 51
print("X:", X)
num_guesses = 0
UPPER = X//2
for i in range(0, UPPER):
    num_guesses += 1
    if i**2 == X:
        print('Number of guesses:', num_guesses)
        break

print()
print("Successive approximation using guess-and-check and bisection methods")
X = 25  # Number of guesses: 13
# X = 2500  # Number of guesses: 20
EPSILON = 0.01  # tolerance of the answer^2 to X

num_guesses = 0
low = 0.0
high = max(X, 1)
ans = (high + low)/2.0

print("X:", X)
print("Tolerance:", EPSILON)

print()
print("LOW, ANSWER, HIGH")
while abs(ans**2 - X) >= EPSILON and ans <= X:
    print(low, ans, high)
    num_guesses += 1
    if ans**2 < X:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0

print()
print(ans, 'is close enough to square root of', X)
print('Number of guesses:', num_guesses)

# LOW, ANSWER, HIGH
# 0.0 12.5 25
# 0.0 6.25 12.5
# 0.0 3.125 6.25
# 3.125 4.6875 6.25
# 4.6875 5.46875 6.25
# 4.6875 5.078125 5.46875
# 4.6875 4.8828125 5.078125
# 4.8828125 4.98046875 5.078125
# 4.98046875 5.029296875 5.078125
# 4.98046875 5.0048828125 5.029296875
# 4.98046875 4.99267578125 5.0048828125
# 4.99267578125 4.998779296875 5.0048828125
# 4.998779296875 5.0018310546875 5.0048828125

# 5.00030517578125 is close enough to square root of 25
# Number of guesses: 13
