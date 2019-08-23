# Generators, Yield:

# Generators are iterators, but can only be iterated over once.
generator1 = (x**2 for x in range(10))
for i in generator1: print i,
# 0 1 4 9 16 25 36 49 64 81
for i in generator1: print i,
# Nothing is printed

# Yield returns a generator.
# Unlike a list, the cubes generator doesn't store any of these items in memory,
# rather the cubed values are computed at runtime, returned, and forgotten.
def cube_numbers(nums):
    for i in nums:
        yield(i**3)

cubes = cube_numbers([1, 2, 3, 4, 5])
next(cubes) # 1
next(cubes) # 8
next(cubes) # 27


# Reversed
for i in reversed(xrange(1,11)):
    print i,
# 10 9 8 7 6 5 4 3 2 1
