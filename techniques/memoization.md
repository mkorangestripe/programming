# Memoization

### Fibonacci sequence using memoization
* The first two numbers in the Fibonacci sequence are either 0,1, or 1,1 depending on the chosen starting point.
* Each subsequent number is the sum of the previous two.
* By using the memo, the order of growth drops from O(2^n) to O(n) for time complexity.

```python
memo0 = {0:0, 1:1}  # 0, 1, 1, 2, 3, 5, 8, 13, 21...
memo1 = {0:1, 1:1}  # 1, 1, 2, 3, 5, 8, 13, 21...

MEMO = memo0

def fibonacci(n, memo):
    """Populate and return the memo dict up to the nth number in the Fibonacci sequence"""
    if not n in memo:
        memo[n] = fibonacci(n-1, MEMO) + fibonacci(n-2, MEMO)
    return memo[n]
```

```python
FIB_NUM = 5

fibonacci(FIB_NUM, MEMO)
print(MEMO[FIB_NUM - 1])  # 3 (the 5th number in memo0)
```

```python
FIB_NUM = 8

fibonacci(FIB_NUM, MEMO)
print(MEMO[FIB_NUM - 1])  # 13 (the 8th number in memo0)
```

### The Golden Ratio
* The golden ration, φ (phi), is about 1.618.
* Line segments 'a' and 'b' where a+b is to 'b' as 'b' is to 'a'
* The higher the numbers in the Fibonacci sequence, the closer their ratio is to the Golden ratio.
* If a Fibonacci number is divided by its immediate predecessor in the sequence, the quotient approximates φ.
* These approximations are alternately lower and higher than φ, and converge on φ as the Fibonacci numbers increase.
* The golden spiral is a logarithmic spiral whose growth factor is φ, the golden ratio.
