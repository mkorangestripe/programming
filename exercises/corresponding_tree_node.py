#!/usr/bin/env python
# Find the corresponding node of a binary tree in a cloned tree.
# Given two binary trees (original and cloned) and a reference to a node target in the original tree...
# return a reference to the same node in the cloned tree.

# Definition for the binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# target = 3
# tree = [7,4,3,null,null,6,19]
btree1 = TreeNode(7)
btree1.left = TreeNode(4)
btree1.right = TreeNode(3)
btree1.right.left = TreeNode(6)
btree1.right.right = TreeNode(19)

btree_clone1 = btree1
target1 = btree1.right


# target = 13
# [23,9,29,null,28,27,19,null,null,null,null,13,1,null,null,26,25,6]
#                         23
#             9                           29
#      null       28             27                 19
#             null null      null null      13               1
#                                       null null      26         25
#                                                    6 null    null null
btree2 = TreeNode(23)
btree2.left = TreeNode(9)
btree2.right = TreeNode(29)
btree2.left.right = TreeNode(28)
btree2.right.left = TreeNode(27)
btree2.right.right = TreeNode(19)
btree2.right.right.left = TreeNode(13)
btree2.right.right.right = TreeNode(1)
btree2.right.right.right.left = TreeNode(26)
btree2.right.right.right.right = TreeNode(25)
btree2.right.right.right.left.left = TreeNode(6)

btree_clone2 = btree2
target2 = btree2.right.right.left


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        if original is None:
            return original

        if original is target:
            return cloned

        left = self.getTargetCopy(original.left, cloned.left, target)

        if left is not None:
            return left

        return self.getTargetCopy(original.right, cloned.right, target)


solution = Solution()
target_clone1 = solution.getTargetCopy(btree1, btree_clone1, target1)
target_clone2 = solution.getTargetCopy(btree2, btree_clone2, target2)
print("target_clone1.val:", target_clone1.val)
print("target_clone2.val:", target_clone2.val)
