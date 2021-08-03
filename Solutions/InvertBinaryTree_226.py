# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
    
        def invert(node: TreeNode):
            if node is None:
                return None
            templeft = invert(node.left)
            tempright = invert(node.right)
            node.left = tempright
            node.right = templeft
            return node
        
        return invert(root)
