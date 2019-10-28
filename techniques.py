## Successive refinement
# http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-4-machine-interpretation-of-a-program/
# Estimating the square root of 'x'

x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(x, 1)
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon and ans <= x:
    print low, high, ans
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0

print 'numGuesses =', numGuesses
print ans, 'is close to square root of', x


## Recursion
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
        if check_remainder(i):
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


# Fibonacci sequence using memoization
# By definition, the first two numbers in the Fibonacci sequence are 1 and 1, or 0 and 1...
# depending on the chosen starting point of the sequence, and each subsequent number is the sum of the previous two.
# By using the memo, the order of growth drops from 2^n to n^2 ???

memo0 = {0:0, 1:1} ## 0, 1, 1, 2, 3, 5, 8, 13, 21
# memo1 = {0:1, 1:1} ## 1, 1, 2, 3, 5, 8, 13, 21
def fibonacci(n):
    if not n in memo0:
        memo0[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo0[n]


# The Golden Ratio
# Line segment of segments 'a' and 'b' where a+b is to 'a' as 'a' is to 'b'.
# The ration is about 1.618.  The higher the numbers in the Fibonacci sqequence, the closer their ratio to the Golden ratio.
# The Greek letter φ (phi) is used to symbolize the golden ratio.
# If a Fibonacci number is divided by its immediate predecessor in the sequence, the quotient approximates φ.
# These approximations are alternately lower and higher than φ, and converge on φ as the Fibonacci numbers increase.
# The golden spiral is a logarithmic spiral whose growth factor is φ, the golden ratio.




## Standard deviation
# A measure that is used to quantify the amount of variation or dispersion of a set of data values.
# A low standard deviation indicates that the data points tend to be close to the mean (also called the expected value) of the set...
# while a high standard deviation indicates that the data points are spread out over a wider range of values.
# Represented by the lower case Greek letter sigma σ for the population standard deviation or the Latin letter s for the sample standard deviation.

# For example a normal distribution (or bell-shaped curve) where each band has a width of 1 standard deviation.

# Gaussian distribution, another term for normal distribution.
# Uniform distribution, sometimes also known as a rectangular distribution, is a distribution that has constant probability.
# Exponential distribution, looks like an arc when graphed.
