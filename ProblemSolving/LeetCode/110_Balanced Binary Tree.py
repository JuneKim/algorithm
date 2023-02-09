# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
            
        def calDepth(node, curr_depth):
            if node == None:
                return curr_depth
            return max(calDepth(node.left, curr_depth + 1), calDepth(node.right, curr_depth+1))
        
        diff = calDepth(root.left, 1) - calDepth(root.right, 1)
        if diff > 1 or diff < -1:
            return False

        lbal = rbal = True
        if root.left is not None:
            lbal = self.isBalanced(root.left)
        if root.right is not None:
            rbal = self.isBalanced(root.right)

        if lbal == True and rbal == True:
            return True

        return False
