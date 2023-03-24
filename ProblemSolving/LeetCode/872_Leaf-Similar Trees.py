# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
## runtime: 84.49%, memory: 35.92%
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def findleaves(node) -> list:
            if node == None:
                return []

            if node.left == None and node.right == None:
                return [node.val]

            li_lftLeaves, li_rgtLeaves = [], []

            if node.left != None:
                li_lftLeaves = findleaves(node.left)
            
            if node.right != None:
                li_rgtLeaves = findleaves(node.right)

            return li_lftLeaves + li_rgtLeaves

        return findleaves(root1) == findleaves(root2)
