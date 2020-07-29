# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        cached = []
        curr = head
        is_cycled = False
        while curr is not None:
            if curr in cached:
                is_cycled = True
                break
            
            cached.append(curr)
            curr = curr.next
            
        return is_cycled
