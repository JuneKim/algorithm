# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# [MJ]
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp_head = head
        while tmp_head is not None:            
            while tmp_head.next is not None and tmp_head.val == tmp_head.next.val:
                tmp_head.next = tmp_head.next.next
            tmp_head = tmp_head.next
        
        return head
