
# Recursion limits

The recursive versions below show the limits of recursion for prime number generators.

```python
from math import sqrt
```

#### Prime number before N

```python
N = 40  # must be greater than 2

primelist = [2]
for i in range(3, N, 2):
    for j in range(2, i):
        if i%j == 0:
            break
        if j == int(sqrt(i)) + 1:
            primelist.append(i)
            break

print("The last prime number before", N, "is", primelist[-1])
```

```
The last prime number before 40 is 37
```

#### Nth prime number

```python
N = 5 #  must be greater than 2

primelist = [2]
i = 3
while len(primelist) < N:
    j = 2
    while i%j != 0:
        if j == int(sqrt(i)) + 1:
            primelist.append(i)
            break
        j+=1
    i+=2

print(f"For N={N}, the prime number is {primelist[-1]}")
```

```
For N=5, the prime number is 11
```

#### Recursive versions

```python
def primegen_recur(primelist, num, divisor, maximum):
    """
    Recursive version, returns list of prime numbers.
    After finding the 62nd prime, maximum recursion depth is exceeded.
    """
    if len(primelist) < maximum:
        if num%divisor != 0:
            if divisor == int(sqrt(num)) + 1:
                primelist.append(num)
                divisor=2
                num+=2
            else:
                divisor+=1
        else:
            divisor=2
            num+=2
        primegen_recur(primelist, num, divisor, maximum)
    return primelist


def primegen_recur2(primelist, num, divisor, maximum):
    """
    Same as primegen_recur, but less indenting.
    Recursive version, returns list of prime numbers.
    After finding the 62nd prime, maximum recursion depth is exceeded.
    """
    if len(primelist) == maximum:
        return primelist
    if num%divisor == 0:
        divisor=2
        num+=2
    elif divisor == int(sqrt(num)) + 1:
        primelist.append(num)
        divisor=2
        num+=2
    else:
        divisor+=1
    primegen_recur2(primelist, num, divisor, maximum)
    return primelist
```

```python
NUM = 3
DIVISOR = 2
MAX = 40
init_primelist = [2]
```

```python
updated_primelist = primegen_recur(init_primelist, NUM, DIVISOR, MAX)
print(updated_primelist)
```

```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173]
```

```python
updated_primelist = primegen_recur2(init_primelist, NUM, DIVISOR, MAX)
print(updated_primelist)
```

```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173]
```
