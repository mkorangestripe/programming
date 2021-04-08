#!/usr/bin/env python
# Smallest Possible int not in Array
# Given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# N is an integer within the range [1..100,000].
# Each element of array A is an integer within the range [−1,000,000..1,000,000].

A1 = [1, 3, 6, 4, 1, 2]
A2 = [1, 2, 3]
A3 = [-1, -3]


def solution(a):
    smallest = 0
    a.sort()
    if a[-1] <= 0:
        return 1
    for i in range(len(a)):
        if a[i] - 1 <= 0:
            continue
        if a[i] == a[i-1]:
            continue
        if a[i] - 1 != a[i-1]:
            smallest = a[i] - 1
    if smallest == 0:
        return a[-1] + 1
    return smallest


print(A1, solution(A1))  # 5
print(A2, solution(A2))  # 4
print(A3, solution(A3))  # 1
