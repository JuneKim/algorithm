# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        
        if root.left == None and root.right == None:
            return
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        tmp_left = root.left
        if tmp_left != None:
            while tmp_left.right != None:
                tmp_left = tmp_left.right
            
            tmp_left.right = root.right
        
            root.right = root.left
            root.left = None
