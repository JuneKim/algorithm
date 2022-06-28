# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def _height(curr_node, curr_height):
            if curr_node is None:
                return curr_height

            left_height = _height(curr_node.left, curr_height + 1)
        
    
            right_height = _height(curr_node.right, curr_height + 1)
    
            return max (left_height, right_height)
        return _height(root, 0)
