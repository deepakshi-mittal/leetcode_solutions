# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        
        def helper(node):
            nonlocal maxpathlen
            if node is None:
                return 0,0
            
            inc_path, dec_path = 1,1 # hanldes base conditions
            
            if node.left:
                left = helper(node.left)
                
                if node.val == node.left.val +1:
                    dec_path = left[1] +1 # if parent is more path is decreasing one
                elif node.val == node.left.val -1:
                    inc_path = left[0] +1 #if parent is less path is increasing one
            if node.right:
                right = helper(node.right)
                
                if node.val ==node.right.val +1:
                    dec_path = max(dec_path, right[1] +1)
                elif node.val == node.right.val -1:
                    inc_path = max(inc_path, right[0]+1)
                    
            maxpathlen = max(maxpathlen, dec_path+inc_path-1) # since root will be countted two times
            
            return [inc_path, dec_path]
        
        maxpathlen =0
        helper(root)
        return maxpathlen
            
            
        
