# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
#         Sentinel nodes are widely used in trees and linked lists as pseudo-heads, pseudo-tails, markers of level end, etc. They are purely functional, and usually does not hold any data. Their main purpose is to standardize the situation, for example, make linked list to be never empty and never headless and hence simplify insert and delete.
        
        curr = head
        sentinel = ListNode(0)
        sentinel.next = head
        # prev = None  not this now we asiggn it sentinel
        prev = sentinel
        
        while(curr):
            if curr.val == val:
                prev.next = curr.next
            else:
                # simply move forward
                prev = curr
            curr = curr.next
        return sentinel.next # this is so because sentinel is never deleted and its next node is always going to be the head node
