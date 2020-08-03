#from typing import List

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        sorted_dict = {}
        curr = head
        while curr is not None:
            sorted_dict[curr.val] = curr
            curr = curr.next
        
        sorted_list = sorted([key for key in sorted_dict.keys()])
        prev = None
        for obj_key in sorted_list[::-1]:
            sorted_dict[obj_key].next = prev
            prev = sorted_dict[obj_key]
            
        return sorted_list[sorted_list[0]]

sol = Solution()
in_data = [4,2,1,3]
head = ListNode(in_data[0], None)
curr = head
for _data in in_data[1:]:
    curr.next = ListNode(_data)
    curr = curr.next

_tmp = sol.sortList(head)

ret_list = list()
while _tmp is not None:
    ret_list.append(_tmp.val)
    _tmp = _tmp.next

print (ret_list)
