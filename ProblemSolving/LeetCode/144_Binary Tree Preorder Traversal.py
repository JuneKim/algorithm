# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        myresult = []
        myresult.append(root.val)
        if root.left != None:
            myresult += self.preorderTraversal(root.left)
        if root.right != None:
            myresult += self.preorderTraversal(root.right)
            

        return myresult
