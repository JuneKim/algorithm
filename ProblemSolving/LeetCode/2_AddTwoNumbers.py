from typing import List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        start_node = None
        result = None
        upcount = 0
        while l1 and l2:
            tmp_val = l1.val + l2.val + upcount
            if tmp_val >= 10:
                upcount = 1
                tmp_val -= 10
            else:
                upcount = 0
            if start_node is None:
                result = ListNode(tmp_val)
                start_node = result
            else:
                result.next = ListNode(tmp_val)
                result = result.next
            l1 = l1.next
            l2 = l2.next
                
        remained = None
        if l1 is not None:
            remained = l1
        elif l2 is not None:
            remained = l2
            
        while remained:
            tmp_val = remained.val + upcount
            if tmp_val >= 10:
                upcount = 1
                tmp_val -= 10
            else:
                upcount = 0
                
            result.next = ListNode(tmp_val)
            
            result = result.next
            remained = remained.next
            
        if upcount:
            result.next = ListNode(upcount)
        
        return start_node
                
                
            
