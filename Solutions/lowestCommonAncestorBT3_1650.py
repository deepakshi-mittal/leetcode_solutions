"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
                
        def findParents(node)->list:
            l = []
            if node is None:
                return l
            l.append(node)
            while(node.parent):
                l.append(node.parent)
                node = node.parent
            return l
                
        p_parents = findParents(p)
        q_parents = findParents(q)
       
        for node1 in q_parents:
            for node2 in p_parents:
                if node1.val == node2.val:
                    return node1
        return None