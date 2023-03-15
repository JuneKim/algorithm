## runtime: 85.77%, memory: 79.61%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ## DFS
        if root == None:
            return None

        lftNode = self.increasingBST(root.left)
        rgtNode = self.increasingBST(root.right)

        if lftNode:
            lastNode = lftNode
            while lastNode.right != None:
                lastNode = lastNode.right
            lastNode.right = root
        else:
            lftNode = root

        if rgtNode:
            root.right = rgtNode
        
        root.left = None
        return lftNode
