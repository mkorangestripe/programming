#!/usr/bin/env python

"""
Searching and Sorting and Time Complexity
Examples from MIT OCW
Examples use sorted and unsorted lists.
Sorting first can be more efficient, but only when doing multiple searches.
"""

import random


# Linear search (unsorted list)
# An unsorted list, at worst must look through all elements.
# O(len(L)) for the loop.  O(1) to test if e == L[i]
# O(n) where n is len(L)

def linear_search(L, e):
    """Linear search"""
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found


# Linear search (sorted list)
# A sorted list, only look until reaching a number greater than e
# O(len(L)) for the loop.  O(1) to test if e == L[i]
# O(n) where n is len(L)

def search(L, e):
    """Linear search (sorted list)"""
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


# Bogo aka Monkey sort
# Example, sort a deck of cards by throwing in air, picking up, and checking if sorted.
# O(n) where n is len(L)
# O(?) worst case, it is unbounded if the deck never randomly sorts.

def bogo_sort(L):
    """Bogo aka Monkey sort"""
    while not is_sorted(L):
        random.shuffle(L)


# Bubble sort
# Consecutive pairs of elements are swapped based on size until the list is sorted.
# Inner loop for comparisons, complexity O(len(L))
# Outer loop for multiple passes until no more swaps, complexity O(len(L))
# O(n^2) where n is len(L)

def bubble_sort(L):
    """Bubble sort"""
    swap = False
    while not swap:
        print('bubble sort: ' + str(L))
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

testList = [1,3,5,7,2,6,25,18,13]

print('')
print(bubble_sort(testList))
print(testList)

# bubble sort: [1, 3, 5, 7, 2, 6, 25, 18, 13]
# bubble sort: [1, 3, 5, 2, 6, 7, 18, 13, 25]
# bubble sort: [1, 3, 2, 5, 6, 7, 13, 18, 25]
# bubble sort: [1, 2, 3, 5, 6, 7, 13, 18, 25]
# None
# [1, 2, 3, 5, 6, 7, 13, 18, 25]


# Selection sort
# The range of the inner loop becomes shorter with each iteration of the outer loop.
# The smallest element is moved to the start of the list and the unsorted portion...
# becomes shorter and shorter.
# O(n^2) where n is len(L)

def selection_sort(L):
    """Selection sort"""
    suffix_st = 0
    while suffix_st != len(L):
        print('selection sort: ' + str(L))
        for i in range(suffix_st, len(L)):
            if L[i] < L[suffix_st]:
                L[suffix_st], L[i] = L[i], L[suffix_st]
        suffix_st += 1

testList = [1,3,5,7,2,6,25,18,13]

print('')
print(selection_sort(testList))
print(testList)

# selection sort: [1, 3, 5, 7, 2, 6, 25, 18, 13]
# selection sort: [1, 3, 5, 7, 2, 6, 25, 18, 13]
# selection sort: [1, 2, 5, 7, 3, 6, 25, 18, 13]
# selection sort: [1, 2, 3, 7, 5, 6, 25, 18, 13]
# selection sort: [1, 2, 3, 5, 7, 6, 25, 18, 13]
# selection sort: [1, 2, 3, 5, 6, 7, 25, 18, 13]
# selection sort: [1, 2, 3, 5, 6, 7, 25, 18, 13]
# selection sort: [1, 2, 3, 5, 6, 7, 13, 25, 18]
# selection sort: [1, 2, 3, 5, 6, 7, 13, 18, 25]
# None
# [1, 2, 3, 5, 6, 7, 13, 18, 25]


# Merge sort
# Uses a divide-and-conquer approach.
# This also uses a depth-first approach by working down the left branch...
# until the two farthest left elements are separated into two sublists each with the one element.
# The pairs of sublists are merged into sorted lists by comparing the first element (remaining) of each.
# This way the sublists will always be sorted.
# O(n log(n)) where n is len(L)

def merge(left, right):
    """Merge sublists"""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right): # this makes the initial comparisons between the right and left lists
        if left[i] < right[j]: # but stops when one list is exhausted.
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left): # if the left sublist has remaining elements, append them to result
        result = result + left[i:]
    if j < len(right): # if the right sublist has remaining elements, append them to result
        result = result + right[j:]
    print('merge: ' + str(left) + '&' + str(right) + ' to ' + str(result))
    return result


def merge_sort(L):
    """Divide-and-conquer depth-first function"""
    print('merge sort: ' + str(L))
    if len(L) < 2:
        return L[:]
    middle = len(L) // 2
    left = merge_sort(L[:middle])
    right = merge_sort(L[middle:])
    return merge(left, right)


testList = [1, 3, 5, 7, 2, 6, 25, 18, 13]

print('')
print(merge_sort(testList))

# merge sort: [1, 3, 5, 7, 2, 6, 25, 18, 13]
# merge sort: [1, 3, 5, 7]
# merge sort: [1, 3]
# merge sort: [1]
# merge sort: [3]
# merge: [1]&[3] to [1, 3]
# merge sort: [5, 7]
# merge sort: [5]
# merge sort: [7]
# merge: [5]&[7] to [5, 7]
# merge: [1, 3]&[5, 7] to [1, 3, 5, 7]
# merge sort: [2, 6, 25, 18, 13]
# merge sort: [2, 6]
# merge sort: [2]
# merge sort: [6]
# merge: [2]&[6] to [2, 6]
# merge sort: [25, 18, 13]
# merge sort: [25]
# merge sort: [18, 13]
# merge sort: [18]
# merge sort: [13]
# merge: [18]&[13] to [13, 18]
# merge: [25]&[13, 18] to [13, 18, 25]
# merge: [2, 6]&[13, 18, 25] to [2, 6, 13, 18, 25]
# merge: [1, 3, 5, 7]&[2, 6, 13, 18, 25] to [1, 2, 3, 5, 6, 7, 13, 18, 25]
# [1, 2, 3, 5, 6, 7, 13, 18, 25]
