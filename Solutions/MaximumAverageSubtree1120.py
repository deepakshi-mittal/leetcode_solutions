# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        if not root:
            return 0
        self.max_avg = float("-inf")
        # [sum_nodes, number_of nodes below]
        def findAvg(node):
            left = [0,0]
            right = [0,0]
            if node is None:
                return [0,0]
            
            if node.left:
                left = findAvg(node.left)
            if node.right:
                right = findAvg(node.right)
    
            nodes = left[1] + right[1] + 1
            sum_t = left[0] + right[0] + node.val
            avg = sum_t/nodes
            self.max_avg = self.max_avg if self.max_avg > avg else avg
            
            return [sum_t, nodes]
        
        findAvg(root)
        
        return self.max_avg
