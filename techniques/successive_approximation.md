# Successive Approximation

```
These examples both estimate the square root of X.
With larger numbers like 2500, the number of guesses is less than half when using the bisection method.
```

#### Simple guess-and-check (exhaustive enumeration)

```python
X = 2500
NUM_GUESSES = 0
UPPER = X//2

print("X:", X)
for i in range(0, UPPER):
    NUM_GUESSES += 1
    if i**2 == X:
        print('Number of guesses:', NUM_GUESSES)
        break
```

```
X: 2500
Number of guesses: 51
```

#### Successive approximation using guess-and-check and bisection method

```python
X = 25
# X = 2500
EPSILON = 0.01  # tolerance of answer^2 to X

NUM_GUESSES = 0
LOW = 0.0
high = max(X, 1)
ans = (high + LOW)/2.0

print("X:", X)
print("Tolerance:", EPSILON)

print()
print("LOW, ANSWER, HIGH")
while abs(ans**2 - X) >= EPSILON and ans <= X:
    print(LOW, ans, high)
    NUM_GUESSES += 1
    if ans**2 < X:
        LOW = ans
    else:
        high = ans
    ans = (high + LOW)/2.0

print()
print(ans, 'is close enough to square root of', X)
print('Number of guesses:', NUM_GUESSES)
```

```
X: 25
Tolerance: 0.01

LOW, ANSWER, HIGH
0.0 12.5 25
0.0 6.25 12.5
0.0 3.125 6.25
3.125 4.6875 6.25
4.6875 5.46875 6.25
4.6875 5.078125 5.46875
4.6875 4.8828125 5.078125
4.8828125 4.98046875 5.078125
4.98046875 5.029296875 5.078125
4.98046875 5.0048828125 5.029296875
4.98046875 4.99267578125 5.0048828125
4.99267578125 4.998779296875 5.0048828125
4.998779296875 5.0018310546875 5.0048828125

5.00030517578125 is close enough to square root of 25
Number of guesses: 13
```
