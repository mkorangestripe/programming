# Various examples

# VM scheduler
def vm_schedule_count(schedule):
    """Determine the number of VMs needed based on the schedule"""
    i,j = 0,0
    for times in schedule:
        start = times[0]
        for prev_times in schedule[i:j]:
            prev_end = prev_times[1]
            if prev_end <= start:
                i += 1
                break
        j += 1
    return len(schedule[i:j])


schedule1 = [(2,5),(3,6),(5,7)]
schedule2 = [(2,5),(3,6),(5,7),(5,8)]
schedule3 = [(2,5),(3,5),(5,7)]
schedule4 = []

vm_schedule_count(schedule1) # 2
vm_schedule_count(schedule2) # 3
vm_schedule_count(schedule3) # 2
vm_schedule_count(schedule4) # 0



# Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example from LeetCode

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


# example runtime: 4624 ms
# example memory: 12.9 MB
nums = [2,7,11,15]
target = 9
bruteforce = BruteForce()
bruteforce.twoSum(nums, target)
# [0, 1]


# example runtime: 1928 ms
# example memory: 13.5 MB
nums = [3,3]
target = 6
twopasshash = TwoPassHash()
twopasshash.twoSum(nums, target)
# [0, 1]


# example runtime: 652 ms
# example memory: 13.1 MB
nums = [3,2,4]
target = 6
onepasshash = OnePassHash()
onepasshash.twoSum(nums, target)



# Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating (duplicate) characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        longest_substring = s[i:j]

        while j < len(s):
            # print(s[j], s[i:j], longest_substring) # testing
            if s[j] not in s[i:j]:
                j += 1
            else:
                for k in s[i:j]:
                    i += 1
                    # print('Searching substring:', k) # testing
                    if k == s[j]:
                        break
            if len(s[i:j]) > len(longest_substring):
                longest_substring = s[i:j]
            # print(i, j) # testing

        # print(longest_substring) # testing
        return len(longest_substring)


# example runtime: 144 ms
# example memory: 13 MB

s1 = "dvdf" # 3
s2 = "aab" # 2
s3 = "bbtablud" # 6
s4 = "pwwkew" # 3
s5 = "dvdf" # 3
s6 = "pwwkewabcdefghijk" # 12

solution = Solution()
solution.lengthOfLongestSubstring(s1)



# Longest Common Prefix
# Given a list of strings, find the longest common prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        num_of_words = len(strs)
        common_prefix = ''

        if num_of_words == 0:
            return common_prefix

        shortest_length = float('inf')
        for word in strs:
            shortest_length = min(shortest_length, len(word))

        char_cnt_list = []
        for j in range(shortest_length):
            char_cnt_list.append(0)
            for word in strs:
                if word[j] != strs[0][j]:
                    break
                char_cnt_list[j] += 1
            if char_cnt_list[j] != num_of_words:
                break
            common_prefix = common_prefix + word[j]

        return common_prefix

# Example runtime: 20 ms
# Example memory: 12 MB


# Binary search method
# Starts by dividing the shortest word in half
# Time complexity: O(S log n) where S is the sum of characters in all strings
# Space complexity: O(1)
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        num_of_words = len(strs)
        if num_of_words == 0:
            return ''

        shortest_len = float('inf')
        for word in strs:
            shortest_len = min(shortest_len, len(word))

        low = 1
        high = shortest_len

        while low <= high:
            mid = (low + high) // 2
            if self.isCommonPrefix(strs, mid):
                low = mid + 1
            else:
                high = mid - 1

        return strs[0][0:((low + high) // 2)]

    def isCommonPrefix(self, strs, mid):
        str1 = strs[0][0:mid]
        i = 1
        while i < len(strs):
            if not strs[i].startswith(str1):
                return False
            i += 1
        return True

# Example runtime: 12 ms
# Example memory: 12 MB


strs1 = ["flower","flow","flight"] # 'fl'
strs2 = ["dog","racecar","car"] # ''
strs3 = ['leets', 'leetcode', 'leetc', 'leeds'] # 'lee'
solution = Solution()
solution.longestCommonPrefix(strs1)
