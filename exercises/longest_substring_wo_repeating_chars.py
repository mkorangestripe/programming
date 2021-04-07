#!/usr/bin/env python
# Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating (duplicate) characters.

s1 = "dvdf"
s2 = "aab"
s3 = "bbtablud"
s4 = "pwwkew"
s5 = "dvdf"
s6 = "pwwkewabcdefghijk"


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


solution = Solution()
solution.lengthOfLongestSubstring(s1)  # 3
solution.lengthOfLongestSubstring(s2)  # 2
solution.lengthOfLongestSubstring(s3)  # 6
solution.lengthOfLongestSubstring(s4)  # 3
solution.lengthOfLongestSubstring(s5)  # 3
solution.lengthOfLongestSubstring(s6)  # 12

# example runtime: 144 ms
# example memory: 13 MB
