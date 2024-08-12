#!/usr/bin/env python

"""
Bisection search examples
Lists must be sorted
Continuously halves the list range to be searched.
O(log n) - reduces the problem by a factor of 2 on each step.
"""

# Bisection search to find x between 1 and 100

def simple_bisect_search(low, high, x):
    num_guesses = 0
    print('x =', x)
    print('low, mid, high:')
    while low != high:
        num_guesses += 1
        mid = (low + high) // 2
        print(low, mid, high)
        if mid == x:
            print('guesses:', num_guesses)
            break
        if (mid + 1) == high: # initial upper bound will never be mid because of floor division
            print('guesses:', num_guesses)
            break
        if mid < x:
            low = mid
        else:
            high = mid

low = 1
high = 100
x_list = [1, 17, 50, 68, 100]
for x in x_list:
    if x < low or x > high:
        print('x is out of bounds')
    else:
        simple_bisect_search(low, high, x)
    print()

# x = 1
# low, mid, high:
# 1 50 100
# 1 25 50
# 1 13 25
# 1 7 13
# 1 4 7
# 1 2 4
# 1 1 2
# guesses: 7

# x = 17
# low, mid, high:
# 1 50 100
# 1 25 50
# 1 13 25
# 13 19 25
# 13 16 19
# 16 17 19
# guesses: 6

# x = 50
# low, mid, high:
# 1 50 100
# guesses: 1

# x = 68
# low, mid, high:
# 1 50 100
# 50 75 100
# 50 62 75
# 62 68 75
# guesses: 4

# x = 100
# low, mid, high:
# 1 50 100
# 50 75 100
# 75 87 100
# 87 93 100
# 93 96 100
# 96 98 100
# 98 99 100
# guesses: 7



# Bisection search to find x in a list

def simple_bisect_search2(L, x, low_i, high_i):
    num_guesses = 0
    print('x =', x)
    print('low, mid, high:')
    while L[low_i] != L[high_i]: # and num_guesses < 100: # testing
        num_guesses += 1
        mid_i = (low_i + high_i) // 2
        # print((low_i, L[low_i]), (mid_i, L[mid_i]), (high_i, L[high_i])) # print index and element
        print(low_i, mid_i, high_i)
        if L[mid_i] == x:
            print('x found at index', mid_i)
            print('guesses:', num_guesses)
            break
        if (mid_i + 1) == high_i: # initial upper bound will never be mid because of floor division
            if L[high_i] == x:
                print('x found at index', high_i)
            else:
                print('x not found')
            print('guesses:', num_guesses)
            break
        if L[mid_i] < x:
            low_i = mid_i
        else:
            high_i = mid_i


# import random
# def create_random_list():
#     L = []
#     for i in range(25):
#         L.append(random.randint(1, 100))
#     L.sort()
#     return L

def run_bisect_search(L, x_list):
    # print(L,'\n')
    low = 0
    high = len(L) - 1
    for x in x_list:
        if x < L[low] or x > L[high]:
            print(x, 'is out of bounds')
        else:
            simple_bisect_search2(L, x, low, high)
        print()


# L = create_random_list()
L = [1, 3, 8, 10, 10, 12, 14, 21, 22, 22, 23, 26, 37,
     45, 54, 54, 55, 58, 64, 68, 71, 81, 89, 90, 100]
x_list = [17, 37, 1, 105, 100, 14]
run_bisect_search(L, x_list)

# x = 17
# low, mid, high:
# 0 12 24
# 0 6 12
# 6 9 12
# 6 7 9
# 6 6 7
# x not found
# guesses: 5

# x = 37
# low, mid, high:
# 0 12 24
# x found at index 12
# guesses: 1

# x = 1
# low, mid, high:
# 0 12 24
# 0 6 12
# 0 3 6
# 0 1 3
# 0 0 1
# x found at index 0
# guesses: 5

# 105 is out of bounds

# x = 100
# low, mid, high:
# 0 12 24
# 12 18 24
# 18 21 24
# 21 22 24
# 22 23 24
# x found at index 24
# guesses: 5

# x = 14
# low, mid, high:
# 0 12 24
# 0 6 12
# x found at index 6
# guesses: 2



# Recursive bisection search to find e in a list

def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        if L[mid] > e:
            if low == mid: # nothing left to search
                return False
            return bisect_search_helper(L, e, low, mid -1)
        return bisect_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    return bisect_search_helper(L, e, 0, len(L) - 1)
