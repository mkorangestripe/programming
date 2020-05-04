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



# Longest Substring (with the following requirements)
# Must not contain a number.
# Contains at least one uppercase letter.
S1 = 'a0Bu'
S2 = 'a0HBu'
S3 = 'a0HBu7qw'
S4 = 'a0HBu7Kqwn'
S5 = 'yf12'


class Solution:
    def lengthOfLongestSubstring(self, s):

        i, j = 0, 0
        longest_substring = s[i:j]
        while j < len(s):
            j += 1
            uppercase_cnt = 0
            for k in s[i:j]:
                if k.isupper():
                    uppercase_cnt += 1
                if k.isdigit():
                    i += 1
            if len(s[i:j]) > len(longest_substring) and uppercase_cnt >= 1:
                longest_substring = s[i:j]

        if len(longest_substring) == 0:
            return -1

        return len(longest_substring), longest_substring


solution = Solution()
print(solution.lengthOfLongestSubstring(S1))  # (2, 'Bu')
print(solution.lengthOfLongestSubstring(S2))  # (3, 'HBu')
print(solution.lengthOfLongestSubstring(S3))  # (3, 'HBu')
print(solution.lengthOfLongestSubstring(S4))  # (4, 'Kqwn')
print(solution.lengthOfLongestSubstring(S5))  # -1



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



# Array Leader
# A non-empty array A consisting of N integers and sorted in a non-decreasing order...
# (i.e. A[0] ≤ A[1] ≤ ... ≤ A[N−1]) is given.
# The leader of this array is the value that occurs in more than half of the elements of A.
# Given a non-empty array A consisting of N integers, sorted in a non-decreasing order, returns the leader of array A.
# The function should return −1 if array A does not contain a leader.

L1 = [2, 2, 2, 2, 2, 3, 4, 4, 4, 6]
L2 = [2, 2, 2, 2, 2, 2, 3, 4, 4, 4, 6]
L3 = [1, 1, 1, 1, 50]


class Solution(object):
    def array_leader(self, arr):
        array_length = len(arr)
        num_hash = {}
        highest_cnt_num = -1
        highest_cnt = 0

        for num in arr:
            if num_hash.has_key(num):
                num_hash[num] = num_hash[num] + 1
            else:
                num_hash[num] = 1

        for num in num_hash:
            if num_hash[num] > highest_cnt:
                highest_cnt = num_hash[num]
                highest_cnt_num = num

        if highest_cnt > (array_length / 2):
            return highest_cnt_num
        else:
            return -1


solution = Solution()
print(solution.array_leader(L1))  # -1
print(solution.array_leader(L2))  # 2
print(solution.array_leader(L3))  # 1



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


print(solution(A1))  # 5
print(solution(A2))  # 4
print(solution(A3))  # 1
