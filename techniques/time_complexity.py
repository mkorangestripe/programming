#!/usr/bin/env python

"""
Orders of Growth of algorithms and Time Complexity
Examples from MIT OWC


Order of Growth:
Describes the increase in time relative to the size of the input
Ignore constants and multiplicative factors
Consider only dominate terms
O(n^2):     n^2 + 2n +2
O(n^2):     n^2 + 10000n + 3^1000
O(n):       log(n) + n + 4
O(n log n): 0.0001*n*log(n) + 300n
O(3^n):     2n^30 + 3^n

for i in range(n): # O(n)
    print('a')

for j in range(n*n): # O(n*n)
    print('b')
O(n) + O(n*n) = O(n+n^2) = O(n^2)

for i in range(n): # O(n)      |
    for j in range(n): # O(n)  |  O(n) * O(n)
        print('a') #           |
O(n) * O(n) = O(n*n) = O(n^2)


Complexity Classes:
c is constant in the examples below
O(1)        constant time
O(log n)    logarithmic time
O(n)        linear time
O(n log n)  log-linear time
O(n^2)      quadratic time (is also polynomial)
O(n^c)      polynomial time (e.g. nested loops or recursive functions)
O(c^n)      exponential time (e.g. Towers of Hanoi)
With exponential complexity, approximate solutions may provide reasonable answers.
"""

# Quadratic complexity O(n^2)
def isSubset(L1, L2):
    """Test whether L1 is a subset of L2"""
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

isSubset(testSet1, testSet)  # True
isSubset(testSet2, testSet)  # False


# Linear example of Bisection search O(n)
# This is the less efficient example of the bisection search - logarithmic O(log n)
# It makes copies of the list instead of using pointers to the list elements.

def bisect_search1(L, e):
    if L == []:
        return False
    if len(L) == 1:
        return L[0] == e

    half = len(L)//2
    if L[half] > e:
        return bisect_search1(L[:half], e)
    return bisect_search1(L[half:], e)


# Iterative and recursive versions of a function with the same complexity
# Both of these compute factorials and both are linear O(n)

def fact_iter(n):
    """compute factorial"""
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod

fact_iter(5)
# 120

def fact_recur(n):
    """assume n >= 0"""
    if n <= 1:
        return 1

    return n*fact_recur(n-1)

fact_recur(5)
# 120


# Exponential complexity O(c^n)
# The smaller the sublist, the larger the number of combinations
# The larger the testSet, the more the sublists

def genSubsets(L):
    """Generate subsets of list L"""
    res = []
    if len(L) == 0:
        return [[]] #list of empty list
    smaller = genSubsets(L[:-1]) # all subsets without last element
    extra = L[-1:] # create a list of just last element
    new = []
    for small in smaller: #                                                              |
        new.append(small+extra)  # for all smaller solutions, add one with last element  |  2^k
    return smaller+new  # combine those with last element and those without              |


testSet = [1,2,3,4]
print(genSubsets(testSet))
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]


# Complexity of an iterative Fibonacci function is linear O(n)
# Complexity of a recursive Fibonacci function without memoization is exponential O(2^n)
