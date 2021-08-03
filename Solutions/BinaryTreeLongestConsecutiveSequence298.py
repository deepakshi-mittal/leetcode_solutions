# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        def findpath(node: TreeNode, parent: TreeNode, length):
            if node is None:
                return  length
            length = length+1 if (parent and node.val == parent.val+1) else 1
            return max(length, max(findpath(node.left, node, length), findpath(node.right, node, length)))
        
        return findpath(root, None ,0)
