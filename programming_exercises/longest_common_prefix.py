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


# Longest Common Prefix (binary search method)
# Starts by dividing the shortest word in half
# Time complexity: O(S log n) where S is the sum of characters in all strings
# Space complexity: O(1)

strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]
strs3 = ['leets', 'leetcode', 'leetc', 'leeds']


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


solution = Solution()
print(solution.longestCommonPrefix(strs1))  # 'fl'
print(solution.longestCommonPrefix(strs2))  # ''
print(solution.longestCommonPrefix(strs3))  # 'lee'

# Example runtime: 12 ms
# Example memory: 12 MB
