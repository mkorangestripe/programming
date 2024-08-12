#!/usr/bin/env python
"""
Remove Duplicates from Beginning of Sorted Array
Modifying the input array in-place with O(1) extra memory.
Duplicate elements may be present after unique elements.
"""

nums1 = []
nums2 = [1]
nums3 = [1, 1]
nums4 = [1, 1, 1]
nums5 = [1, 1, 1, 1]
nums6 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        i, j = 0, 0
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i+1] = nums[j]
                i += 1
                j += 1

        return (i + 1, nums)  # testing
        # return i + 1


solution = Solution()
print(solution.removeDuplicates(nums1))  # 0
print(solution.removeDuplicates(nums2))  # (1, [1])
print(solution.removeDuplicates(nums3))  # (1, [1, 1])
print(solution.removeDuplicates(nums4))  # (1, [1, 1, 1])
print(solution.removeDuplicates(nums5))  # (1, [1, 1, 1, 1])
print(solution.removeDuplicates(nums6))  # (5, [0, 1, 2, 3, 4, 2, 2, 3, 3, 4])


# Runtime: 88 ms
# Memory Usage: 15.6 MB


# A solution using 'set'
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
id(nums)  # 140626277373024
nums[:] = list(set(nums))
nums  # [0, 1, 2, 3, 4]
id(nums)  # 140626277373024

# Runtime: 80 ms
# Memory Usage: 15.7 MB
