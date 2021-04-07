#!/usr/bin/env python
# Array Leader
# A non-empty array A consisting of N integers and sorted in a non-decreasing order...
# (i.e. A[0] ≤ A[1] ≤ ... ≤ A[N−1]) is given.
# The leader of this array is the value that occurs in more than half of the elements of A.
# Given a non-empty array A consisting of N integers, sorted in a non-decreasing order, returns the leader of array A.
# The function should return −1 if array A does not contain a leader.

L1 = [2, 2, 2, 2, 2, 3, 4, 4, 4, 6]
L2 = [2, 2, 2, 2, 2, 2, 3, 4, 4, 4, 6]
L3 = [1, 1, 1, 1, 50]


class Solution:
    def array_leader(self, arr):
        array_length = len(arr)
        num_hash = {}
        highest_cnt_num = -1
        highest_cnt = 0

        for num in arr:
            if num in num_hash.keys():
                num_hash[num] = num_hash[num] + 1
            else:
                num_hash[num] = 1

        for num in num_hash:
            if num_hash[num] > highest_cnt:
                highest_cnt = num_hash[num]
                highest_cnt_num = num

        if highest_cnt > (array_length / 2):
            return highest_cnt_num
        return -1


solution = Solution()
print(solution.array_leader(L1))  # -1
print(solution.array_leader(L2))  # 2
print(solution.array_leader(L3))  # 1
