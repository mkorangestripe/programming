#!/usr/bin/env python
"""
Two Element Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""


# Brute Force
# Time complexity: O(n^2)
# Space complexity: O(1)
class BruteForce:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_of_nums = len(nums)
        for i in range(len_of_nums):
            for j in range(i+1, len_of_nums):
                if nums[i] + nums[j] == target:
                    return [i,j]


# Two-pass Hash Table
# Time complexity: O(n)
# Space complexity: O(n)
class TwoPassHash:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_hash = {}

        # num_hash = {3:1}
        for i in range(len(nums)):
            num_hash[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_hash.keys() and num_hash[complement] != i:
                return [i, num_hash[complement]]


# One-pass Hash Table
# Time complexity: O(n)
# Space complexity: O(n)
class OnePassHash:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_hash = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_hash.keys():
                return [num_hash[complement], i]
            num_hash[nums[i]] = i


nums = [2,7,11,15]
TARGET = 9
bruteforce = BruteForce()
complements = bruteforce.twoSum(nums, TARGET)
print("BruteForce")
print("Target:", TARGET)
print("Array:", nums)
print("Complementary indices:", complements)
print()
# complementary indices: [0, 1]
# example runtime: 4624 ms
# example memory: 12.9 MB

nums = [3,3]
TARGET = 6
twopasshash = TwoPassHash()
complements = twopasshash.twoSum(nums, TARGET)
print("TwoPassHash")
print("Target:", TARGET)
print("Array:", nums)
print("Complementary indices:", complements)
print()
# complementary indices: [0, 1]
# example runtime: 1928 ms
# example memory: 13.5 MB

nums = [3,2,4]
TARGET = 6
onepasshash = OnePassHash()
complements = onepasshash.twoSum(nums, TARGET)
print("OnePassHash")
print("Target:", TARGET)
print("Array:", nums)
print("Complementary indices:", complements)
# complementary indices: [1, 2]
# example runtime: 652 ms
# example memory: 13.1 MB
