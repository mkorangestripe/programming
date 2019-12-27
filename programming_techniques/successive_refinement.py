# Successive refinement
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
