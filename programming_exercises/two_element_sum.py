# Two Element Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


# Brute Force
# Time complexity: O(n^2)
# Space complexity: O(1)
class BruteForce(object):
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
class TwoPassHash(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_hash = {}

        for i in range(len(nums)):
            num_hash[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_hash.keys() and num_hash[complement] != i:
                return [i, num_hash[complement]]


# One-pass Hash Table
# Time complexity: O(n)
# Space complexity: O(n)
class OnePassHash(object):
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
target = 9
bruteforce = BruteForce()
bruteforce.twoSum(nums, target)
# [0, 1]
# example runtime: 4624 ms
# example memory: 12.9 MB

nums = [3,3]
target = 6
twopasshash = TwoPassHash()
twopasshash.twoSum(nums, target)
# [0, 1]
# example runtime: 1928 ms
# example memory: 13.5 MB

nums = [3,2,4]
target = 6
onepasshash = OnePassHash()
onepasshash.twoSum(nums, target)
# [1, 2]
# example runtime: 652 ms
# example memory: 13.1 MB
