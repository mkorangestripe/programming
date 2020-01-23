# Order of Growth
# Describes the increase in time relative to the size of the input
# Ignore constants and multiplicative factors
# Consider only dominate terms
# O(n^2):     n^2 + 2n +2
# O(n^2):     n^2 + 10000n + 3^1000
# O(n):       log(n) + n + 4
# O(n log n): 0.0001*n*log(n) + 300n
# O(3^n):     2n^30 + 3^n

for i in range(n): # O(n)
    print('a')
for j in range(n*n): # O(n*n)
    print('b')
# O(n) + O(n*n) = O(n+n^2) = O(n^2)

for i in range(n): # O(n)      |
    for j in range(n): # O(n)  |  O(n) * O(n)
        print('a') #           |
# O(n) * O(n) = O(n*n) = O(n^2)

# Complexity Classes
# O(1)        constant time
# O(log n)    logarithmic time
# O(n)        linear time
# O(n log n)  log-linear time
# O(n^2)      quadratic time
# O(n^c)      polynomial time (c is constant)
# O(c^n)      exponential time (constant raised to a power based on size of input)

# Quadratic complexity
def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True

testSet = [1, 2, 3, 4, 5]
testSet1 = [1, 5, 3]
testSet2 = [1, 6]

isSubset(testSet1, testSet)
# True
isSubset(testSet2, testSet)
# False

# Bisection search - linear O(n)
# This is the less efficient example of the bisection search - logarithmic O(log n).
# It makes copies of the list instead of using pointers to the list elements.

def bisect_search1(L, e):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2
        if L[half] > e:
            return bisect_search1(L[:half], e)
        else:
            return bisect_search1(L[half:], e)
