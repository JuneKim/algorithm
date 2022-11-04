# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# MJ
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        return self.splitArray(nums)

    def splitArray(self, split_nums: List[int]):
        array_len = len(split_nums)
        if array_len == 0:
            return None
        elif array_len == 1:
            return TreeNode(split_nums[0])
        elif array_len == 2:
            return TreeNode(split_nums[1], TreeNode(split_nums[0]), None)
        
        median_idx = len(split_nums)//2
        median_node = TreeNode(split_nums[median_idx])
        median_node.left = self.splitArray(split_nums[:median_idx])
        median_node.right = self.splitArray(split_nums[median_idx + 1:])

        return median_node
            
#class Solution:
#    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#       li_len = len(nums)
#       if li_len == 0:
#           return None
#
#       return TreeNode(nums[li_len//2], sortedArrayToBST(nums[:li_len//2], sortedArrayToBST[li_len+1:])
#
#
#
