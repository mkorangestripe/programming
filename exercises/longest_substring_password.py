#!/usr/bin/env python
"""
Longest Substring (with the following requirements)
Must not contain a number.
Contains at least one uppercase letter.
"""

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
print(S1, solution.lengthOfLongestSubstring(S1))  # (2, 'Bu')
print(S2, solution.lengthOfLongestSubstring(S2))  # (3, 'HBu')
print(S3, solution.lengthOfLongestSubstring(S3))  # (3, 'HBu')
print(S4, solution.lengthOfLongestSubstring(S4))  # (4, 'Kqwn')
print(S5, solution.lengthOfLongestSubstring(S5))  # -1
