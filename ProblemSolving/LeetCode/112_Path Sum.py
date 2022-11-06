# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False                      
            
        return self.dfs(root, 0, targetSum)
        
        
    def dfs(self, node: TreeNode, currentSum: int, targetSum: int) -> int:
        if node == None:
            return False
        
        if node.left == None and node.right == None: # leaf
            if targetSum == node.val + currentSum:
                return True
            else:
                return False
        
        left_ret = self.dfs(node.left, currentSum + node.val, targetSum)
        right_ret = self.dfs(node.right, currentSum + node.val, targetSum)

        return (left_ret | right_ret)
