#!/usr/bin/env python
"""
Given a binary tree, return the sum of values of its deepest leaves.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
btree = TreeNode(1)
btree.left = TreeNode(2)
btree.right = TreeNode(3)
btree.left.left = TreeNode(4)
btree.left.right = TreeNode(5)
btree.right.right = TreeNode(6)
btree.left.left.left = TreeNode(7)
btree.right.right.right = TreeNode(8)


class Solution:

    def deepestLeavesSum(self, root: TreeNode) -> int:
        depth = 0
        total = 0

        def sumTree(root, curdepth):
            nonlocal depth
            nonlocal total

            if root is None:
                return

            if curdepth > depth:
                depth = curdepth
                total = root.val
            elif curdepth == depth:
                total += root.val

            sumTree(root.left, curdepth + 1)
            sumTree(root.right, curdepth + 1)

        sumTree(root, depth)
        return total


solution = Solution()
deepest_leaves_sum = solution.deepestLeavesSum(btree)
print("Sum of deepest leaves:", deepest_leaves_sum)  # Sum of deepest leaves: 15
