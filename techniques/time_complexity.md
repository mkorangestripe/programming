## Orders of Growth and Time Complexity  

#### Orders of Growth

```
Describes the increase in time relative to the size of the input.
Ignore constants and multiplicative factors.
Consider only the dominate terms.

O(n^2)      n^2 + 2n +2
O(n^2)      n^2 + 10000n + 3^1000
O(n)        log(n) + n + 4
O(n log n)  0.0001*n*log(n) + 300n
O(3^n)      2n^30 + 3^n
```

```python
for i in range(n):  # O(n)
    print('a')

for j in range(n*n):  # O(n*n)
    print('b')
# O(n) + O(n*n) = O(n+n^2) = O(n^2)

for i in range(n):      # O(n)
    for j in range(n):  # O(n) - with outer loop: O(n) * O(n)
        print('a')
# O(n) * O(n) = O(n*n) = O(n^2)
```

#### Complexity Classes

```
O(1)        constant time
O(log n)    logarithmic time
O(n)        linear time
O(n log n)  log-linear time
O(n^2)      quadratic time (is also polynomial)
O(n^c)      polynomial time (e.g. nested loops or recursive functions)
O(c^n)      exponential time (e.g. Towers of Hanoi)

The c is constant.  
With exponential complexity, approximate solutions may provide reasonable answers.
```

#### Quadratic complexity O(n^2)

```python
def is_subset(list1, list2):
    """Test whether list1 is a subset of list2"""
    for e1 in list1:
        matched = False
        for e2 in list2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True

testSet = [1, 2, 3, 4, 5]
testSet1 = [1, 5, 3]
testSet2 = [1, 6]

print(is_subset(testSet1, testSet))  # True
print(is_subset(testSet2, testSet))  # False
```

#### Linear Bisection search O(n)

```python
# This is the less efficient example of the bisection search - logarithmic O(log n)
# It makes copies of the list instead of using pointers to the list elements.

def bisect_search1(list1, e):
    """Linear Bisection search"""
    if list1 == []:
        return False
    if len(list1) == 1:
        return list1[0] == e

    half = len(list1)//2
    if list1[half] > e:
        return bisect_search1(list1[:half], e)
    return bisect_search1(list1[half:], e)
```

#### Iterative compute factorial O(n)

```python
def fact_iter(n):
    """Compute factorial"""
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod

fact_iter(5)  # 120
```

#### Recursive compute factorial O(n)

```python
def fact_recur(n):
    """
    Compute factorial
    Assume n >= 0
    """
    if n <= 1:
        return 1

    return n*fact_recur(n-1)

fact_recur(5)  # 120
```

#### Exponential complexity O(c^n)

```python
# The smaller the sublist, the larger the number of combinations.
# The larger the testSet, the more the sublists.

def gen_subsets(list1):
    """Generate subsets of list1"""
    if len(list1) == 0:
        return [[]]  # list of empty list
    smaller = gen_subsets(list1[:-1])  # all subsets without last element
    extra = list1[-1:]  # create a list of just last element
    new = []
    for small in smaller:
        new.append(small+extra)  # for all smaller solutions, add one with last element - 2^k
    return smaller+new  # combine those with last element and those without

testSet = [1,2,3,4]
gen_subsets(testSet)
```

```
[[],
 [1],
 [2],
 [1, 2],
 [3],
 [1, 3],
 [2, 3],
 [1, 2, 3],
 [4],
 [1, 4],
 [2, 4],
 [1, 2, 4],
 [3, 4],
 [1, 3, 4],
 [2, 3, 4],
 [1, 2, 3, 4]]
```

```
Complexity of an iterative Fibonacci function is linear O(n)
Complexity of a recursive Fibonacci function without memoization is exponential O(2^n)
```
