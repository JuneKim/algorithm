# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
## runtime: 88.19%, memory: 46.51%
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # breath first search
        if root == None:
            return None

        if root.left != None:
            self.invertTree(root.left)
        
        if root.right != None:
            self.invertTree(root.right)

        tmp = root.right
        root.right = root.left
        root.left = tmp

        return root
