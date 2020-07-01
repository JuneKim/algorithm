# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        curr = None
        
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
             
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                tmp = ListNode(l1.val)
                l1 = l1.next
            else:
                tmp = ListNode(l2.val)
                l2 = l2.next
            if head is None:
                head = tmp
                curr = head
            else:
                curr.next = tmp
                curr = tmp
                
        if l1 is not None:
            curr.next = l1
        elif l2 is not None:
            curr.next = l2
        return head   
