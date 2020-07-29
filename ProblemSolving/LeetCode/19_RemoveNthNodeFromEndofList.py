# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = head
        candidate = head
        prev = None
        curr_idx = 0
        while curr.next is not None:
            curr_idx += 1
            if curr_idx >= n:
                prev = candidate
                candidate = candidate.next
                   
            curr = curr.next
        if prev == None:
            head = head.next
        else:
            prev.next = candidate.next   
            
        return head
