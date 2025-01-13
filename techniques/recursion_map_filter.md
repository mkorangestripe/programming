# Recursion

### Map

```python
def cube(x):
    """Return x cubed"""
    return x**3
```

Map functions

```python
def map_iter(f, num_list):
    """Iterative map function"""
    cubes = []
    for i in num_list:
        cubes.append(f(i))
    return cubes

def map_recur_lx(f, num_list):
    """Recursive map function, pass shortened copy of list"""
    if len(num_list) != 0:
        num, num_list = num_list[0], num_list[1:]
        cubes.append(f(num))
        map_recur_lx(f, num_list)
    return cubes

def map_recur_idx(f, num_list, i=0):
    """Recursive map function, pass index"""
    if len(num_list[i:]) != 0:
        num = num_list[i]
        cubes.append(f(num))
        i+=1
        map_recur_idx(f, num_list, i)
    return cubes
```

```python
list1 = [1,2,3]

map_iter(cube, list1)       # [1, 8, 27]

cubes = []
map_recur_lx(cube, list1)   # [1, 8, 27]

cubes = []
map_recur_idx(cube, list1)  # [1, 8, 27]

# cubes = [] could alternatively be inside a wrapper function
```

```python
list1 = [1,2,3]

# Using the builtin map function:
list(map(cube, list1))        # [1, 8, 27]

# As a list comprehension:
[cube(num) for num in list1]  # [1, 8, 27]
```

Also see recursive prime number generator examples.

### Filter

```python
def check_remainder(x):
    """Return x when not evenly divisible by 2 or 3"""
    return x % 2 != 0 and x % 3 != 0
```

Filter functions

```python
def filter_iter(f, num_list):
    """Iterative filter function"""
    no_remainder = []
    for i in num_list:
        if f(i):
            no_remainder.append(i)
    return no_remainder

def filter_recur(f, num_list):
    """Recursive filter function"""
    if len(num_list) != 0:
        num, num_list = num_list[0], num_list[1:]
        if f(num):
            no_remainders.append(num)
        filter_recur(f, num_list)
    return no_remainders
```

```python
list2 = range(2, 25)

filter_iter(check_remainder, list2)   # [5, 7, 11, 13, 17, 19, 23]

no_remainders = []
filter_recur(check_remainder, list2)  # [5, 7, 11, 13, 17, 19, 23]

# no_remainders = [] could alternatively be inside a wrapper function
```

```python
list2 = range(2, 25)

# As a list comprehension:
[num for num in list2 if check_remainder(num)]  # [5, 7, 11, 13, 17, 19, 23]
```
